import unittest
from glab import find_bridge_words, create_graph, process_text


class TestBridgeWords(unittest.TestCase):

    def setUp(self):
        text = "To explore out strange new worlds, To seek out new life and new civilizations?"
        self.words = process_text(text)
        self.G = create_graph(self.words)

    def test_with_bridge_word1(self):
        # 测试用例 1
        result = find_bridge_words(self.G, 'zxq', 'lb')
        expected_output = False
        self.assertEqual(result, expected_output)

    def test_with_bridge_word2(self):
        # 测试用例 2
        result = find_bridge_words(self.G, 'zxq', 'life')
        expected_output = False
        self.assertEqual(result, expected_output)

    def test_with_bridge_word3(self):
        # 测试用例 3
        result = find_bridge_words(self.G, 'explore', 'lb')
        expected_output = False
        self.assertEqual(result, expected_output)

    def test_with_bridge_word4(self):
        # 测试用例 4
        result = find_bridge_words(self.G, 'seek', 'out')
        expected_output = False
        self.assertEqual(result, expected_output)

    def test_with_bridge_word5(self):
        # 测试用例 5
        result = find_bridge_words(self.G, 'To', 'out')
        expected_output = ['explore', 'seek']
        self.assertEqual(result, expected_output)

    def test_with_bridge_word6(self):
        # 测试用例 6
        result = find_bridge_words(self.G, 'seek', 'new')
        expected_output = ['out']
        self.assertEqual(result, expected_output)



if __name__ == '__main__':
    unittest.main()
