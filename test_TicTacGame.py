import unittest
from TicTac import TicTacGame


class TicTacGameTestCase(unittest.TestCase):
    """Тесты для класса TicTacGame"""

    def setUp(self) -> None:
        """Создание экземпляра игры"""
        self.game = TicTacGame()

    def test_filling_array(self) -> None:
        """Тестирование заполнения массива"""
        self.game.filling_array(0, 0)
        self.game.filling_array(1, 1)
        self.assertNotEqual(self.game.mas[0][0], 0)
        self.assertNotEqual(self.game.mas[1][1], 0)

    def test_check_winner_continue(self) -> None:
        """Тестирование определения победителя (продолжение игры)"""
        self.game.mas[0][0] = 'x'
        self.game.mas[1][0] = 'o'
        result = self.game.check_winner('x')
        self.assertEqual(result, False)

    def test_check_winner_diagonal(self) -> None:
        """Тестирование определения победителя (проверка по диагоняли)"""
        self.game.mas[0][0] = 'x'
        self.game.mas[1][1] = 'x'
        self.game.mas[2][2] = 'x'
        result = self.game.check_winner('x')
        self.assertEqual(result, 'x')

    def test_check_winner_row(self) -> None:
        """Тестирование определения победителя (проверка по строке)"""
        self.game.mas[0][0] = 'x'
        self.game.mas[0][1] = 'x'
        self.game.mas[0][2] = 'x'
        result = self.game.check_winner('x')
        self.assertEqual(result, 'x')

    def test_check_winner_col(self) -> None:
        """Тестирование определения победителя (проверка по столбцу)"""
        self.game.mas[0][0] = 'x'
        self.game.mas[1][0] = 'x'
        self.game.mas[2][0] = 'x'
        result = self.game.check_winner('x')
        self.assertEqual(result, 'x')

    def test_check_winner_draw(self) -> None:
        """Тестирование определения победителя (ничья)"""
        self.game.mas[0][0] = 'x'
        self.game.mas[0][1] = 'x'
        self.game.mas[1][2] = 'x'
        self.game.mas[2][1] = 'x'
        self.game.mas[2][0] = 'x'
        self.game.mas[0][2] = 'o'
        self.game.mas[1][0] = 'o'
        self.game.mas[1][1] = 'o'
        self.game.mas[2][2] = 'o'
        result = self.game.check_winner('x')
        self.assertEqual(result, 'Draw')


if __name__ == '__name__':
    unittest.main()
