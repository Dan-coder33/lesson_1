import sys
import pygame


class TicTacGame:
    """Класс игры в крустики-нолики"""
    pygame.init()
    size_block = 100
    margin = 15
    width = height = size_block * 3 + margin * 4
    size_window = (width, height)
    screen = pygame.display.set_mode(size_window)
    pygame.display.set_caption("Tic-Tac")
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)
    mas = [[0] * 3 for _ in range(3)]
    query = 0
    game_over = False

    def show_board(self) -> None:
        """Метод отрисовки игрового поля"""
        for row in range(3):
            for col in range(3):
                if self.mas[row][col] == 'x':
                    color = self.red
                elif self.mas[row][col] == 'o':
                    color = self.green
                else:
                    color = self.white

                x = col * self.size_block + (col + 1) * self.margin
                y = row * self.size_block + (row + 1) * self.margin
                pygame.draw.rect(
                    self.screen, color,
                    (x, y, self.size_block, self.size_block)
                )
                if color == self.red:
                    pygame.draw.line(
                        self.screen, self.white, (x + 5, y + 5),
                        (x + self.size_block - 5, y + self.size_block - 5), 3
                    )
                    pygame.draw.line(
                        self.screen, self.white,
                        (x + self.size_block - 5, y + 5),
                        (x + 5, y + self.size_block - 5), 3
                    )
                elif color == self.green:
                    pygame.draw.circle(
                        self.screen, self.white,
                        (x + self.size_block // 2, y + self.size_block // 2),
                        self.size_block // 2 - 3, 3
                    )

    def event_handler(self) -> None:
        """Метод обработки событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and not self.game_over
            ):
                x_mouse, y_mouse = pygame.mouse.get_pos()
                col = x_mouse // (self.size_block + self.margin)
                row = y_mouse // (self.size_block + self.margin)
                try:
                    self.filling_array(row, col)
                except IndexError:
                    print('Вы вышли за пределы клетки!')

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if self.query % 2 == 0:
                    print('Ход 1 игрока')
                else:
                    print('Ход 2 игрока')
                try:
                    input_row = int(input('Введите номер строки: '))
                    input_col = int(input('Введите номер столбца: '))
                    self.filling_array(input_row - 1, input_col - 1)
                except (IndexError, ValueError): 
                    print('Неправильный формат ввода!')

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.game_over = False
                self.mas = [[0] * 3 for _ in range(3)]
                self.query = 0
                self.screen.fill(self.black)

    def filling_array(self, row: int, col: int) -> None:
        if self.mas[row][col] == 0:
            if self.query % 2 == 0:
                self.mas[row][col] = 'x'
            else:
                self.mas[row][col] = 'o'
            self.query += 1

    def start_game(self) -> None:
        """Метод запуска игры"""
        while True:
            self.event_handler()
            if not self.game_over:
                self.show_board()

            if (self.query - 1) % 2 == 0:
                self.game_over = self.check_winner('x')
            else:
                self.game_over = self.check_winner('o')

            self.check_game_over()

            pygame.display.update()

    def check_game_over(self) -> None:
        if self.game_over:
            self.screen.fill(self.black)
            font = pygame.font.SysFont('stxingkai', 80)
            text1 = font.render(self.game_over, True, self.white)
            text_rect = text1.get_rect()
            text_x = int(self.screen.get_width() / 2 - text_rect.width / 2)
            text_y = int(self.screen.get_height() / 2 - text_rect.height / 2)
            self.screen.blit(text1, [text_x, text_y])

    def check_winner(self, sign: str):
        """Метод определения победителя"""
        zeroes = 0
        for row in self.mas:
            zeroes += row.count(0)
            if row.count(sign) == 3:
                return sign

        for col in range(3):
            if (
                    self.mas[0][col] == sign
                    and self.mas[1][col] == sign
                    and self.mas[2][col] == sign
            ):
                return sign

        if (
                self.mas[0][0] == sign
                and self.mas[1][1] == sign
                and self.mas[2][2] == sign
        ):
            return sign

        if (
                self.mas[0][2] == sign
                and self.mas[1][1] == sign
                and self.mas[2][0] == sign
        ):
            return sign

        if zeroes == 0:
            return 'Draw'

        return False


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
