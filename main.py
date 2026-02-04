import os
import sys
import json
from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.markdown import Markdown

import llm_client
import interpreter
import tool_set

# Initialize Rich Console
console = Console()

def main():
    load_dotenv()
    
    if not os.getenv("OPENROUTER_API_KEY"):
        console.print("[bold red]Error:[/bold red] OPENROUTER_API_KEY is not set.")
        console.print("Please create a .env file with your API key based on .env.example")
        return

    console.print(Panel.fit("[bold cyan]Gemini Robot CLI[/bold cyan]\nType 'exit' or 'quit' to stop.", border_style="cyan"))

    # Context management (simple history)
    # We could maintain a list of messages if we want multi-turn conversation.
    # For now, we'll keep it simple per request, or basic history if needed.
    
    while True:
        try:
            user_input = Prompt.ask("\n[bold green]You[/bold green]")
            if user_input.lower() in ['exit', 'quit']:
                console.print("[yellow]Goodbye![/yellow]")
                break
            
            if not user_input.strip():
                continue

            with console.status("[bold blue]Thinking...[/bold blue]"):
                tools = tool_set.get_tools_definition()
                response = llm_client.query_gemini(user_input, tools)
                parsed = llm_client.parse_llm_response(response)

            if "error" in parsed:
                console.print(f"[bold red]Error from LLM:[/bold red] {parsed['error']}")
                if "raw" in parsed:
                    console.print(parsed['raw'])
                continue

            content_type = parsed.get("type")
            
            if content_type == "message":
                console.print(Markdown(parsed["content"]))
                
            elif content_type == "tool_calls":
                tool_calls = parsed["content"]
                console.print(f"[bold yellow]Plan:[/bold yellow] The assistant wants to perform {len(tool_calls)} action(s).")
                
                for tc in tool_calls:
                    func_name = tc['function']['name']
                    args = tc['function']['arguments']
                    console.print(f"  - Call [bold cyan]{func_name}[/bold cyan] with arguments: {args}")

                # Safety Check
                if Confirm.ask("Do you want to proceed with these actions?"):
                    for tc in tool_calls:
                        func_name = tc['function']['name']
                        with console.status(f"Executing {func_name}..."):
                            result = interpreter.execute_tool_call(tc)
                        
                        console.print(f"[bold green]Result ({func_name}):[/bold green]")
                        console.print(result)
                else:
                    console.print("[yellow]Action cancelled.[/yellow]")

        except KeyboardInterrupt:
            console.print("\n[yellow]Goodbye![/yellow]")
            break
        except Exception as e:
            console.print(f"[bold red]Unexpected Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
