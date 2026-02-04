import os
import shutil
import tool_set
import unittest

class TestToolSet(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_playground"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)
        
        # Create dummy files
        with open(os.path.join(self.test_dir, "doc1.pdf"), "w") as f: f.write("dummy pdf")
        with open(os.path.join(self.test_dir, "doc2.txt"), "w") as f: f.write("dummy txt")
        with open(os.path.join(self.test_dir, "image.png"), "w") as f: f.write("dummy png")
        
        os.makedirs(os.path.join(self.test_dir, "subfolder"))
        with open(os.path.join(self.test_dir, "subfolder", "doc3.pdf"), "w") as f: f.write("dummy pdf deep")

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_find_files(self):
        print("\nTesting find_files...")
        results = tool_set.find_files("*.pdf", self.test_dir)
        self.assertEqual(len(results), 2, "Should find 2 PDFs")
        print("Found:", results)

    def test_move_files(self):
        print("\nTesting move_files...")
        pdfs = tool_set.find_files("*.pdf", self.test_dir)
        dest = os.path.join(self.test_dir, "all_pdfs")
        
        result = tool_set.move_files(pdfs, dest)
        self.assertEqual(len(result["success"]), 2)
        
        # Verify move
        self.assertTrue(os.path.exists(os.path.join(dest, "doc1.pdf")))
        self.assertTrue(os.path.exists(os.path.join(dest, "doc3.pdf")))
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, "doc1.pdf")))

if __name__ == '__main__':
    unittest.main()
