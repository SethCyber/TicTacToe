import pygame

import time

import TicTacToe

exclamation_count = 0

pygame.init()

width, height = 300, 300

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Tic Tac Toe")

rect_width, rect_height = 100, 100

rect_color = (0, 0, 0)

rect_x, rect_y = 0, 0

screen.fill((255, 255, 255))

pygame.draw.rect(screen, (217, 217, 214), (0, 0, 100, 100))

pygame.draw.rect(screen, (217, 217, 214), (100, 100, 100, 100))

pygame.draw.rect(screen, (217, 217, 214), (200, 200, 100, 100))

pygame.draw.rect(screen, (217, 217, 214), (200, 0, 100, 100))

pygame.draw.rect(screen, (217, 217, 214), (0, 200, 100, 100))

x = pygame.image.load('x.png')
o = pygame.image.load('o.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if mouse_position[0] <= 100 and mouse_position[1] <= 100:
                if TicTacToe.move('top-left'):
                    TicTacToe.display_board()
                    TicTacToe.alternate_turn()
                    if TicTacToe.turn:
                        screen.blit(o, (0, 0))
                        pygame.display.flip()
                        pygame.display.update()
                    else:
                        screen.blit(x, (0, 0))
                        pygame.display.flip()
                        pygame.display.update()
            elif 200 >= mouse_position[0] >= 100 >= mouse_position[1]:
                if TicTacToe.move('top-center'):
                    TicTacToe.display_board()
                    TicTacToe.alternate_turn()
                    if TicTacToe.turn:
                        screen.blit(o, (100, 0))
                        pygame.display.flip()
                        pygame.display.update()
                    else:
                        screen.blit(x, (100, 0))
                        pygame.display.flip()
                        pygame.display.update()
            elif 300 >= mouse_position[0] >= 200 and mouse_position[1] <= 100:
                if TicTacToe.move('top-right'):
                    TicTacToe.display_board()
                    TicTacToe.alternate_turn()
                    if TicTacToe.turn:
                        screen.blit(o, (200, 0))
                        pygame.display.flip()
                        pygame.display.update()
                    else:
                        screen.blit(x, (200, 0))
                        pygame.display.flip()
                        pygame.display.update()
            elif mouse_position[0] <= 100 and 100 <= mouse_position[1] <= 200:
                if TicTacToe.move('middle-left'):
                    TicTacToe.display_board()
                    TicTacToe.alternate_turn()
                    if TicTacToe.turn:
                        screen.blit(o, (0, 100))
                        pygame.display.flip()
                        pygame.display.update()
                    else:
                        screen.blit(x, (0, 100))
                        pygame.display.flip()
                        pygame.display.update()
            elif 100 <= mouse_position[0] <= 200 and 100 <= mouse_position[1] <= 200:
                if TicTacToe.move('middle-center'):
                    TicTacToe.display_board()
                    TicTacToe.alternate_turn()
                    if TicTacToe.turn:
                        screen.blit(o, (100, 100))
                        pygame.display.flip()
                        pygame.display.update()
                    else:
                        screen.blit(x, (100, 100))
                        pygame.display.flip()
                        pygame.display.update()
            elif 200 <= mouse_position[0] <= 300 and 100 <= mouse_position[1] <= 200:
                if TicTacToe.move('middle-right'):
                    TicTacToe.display_board()
                    TicTacToe.alternate_turn()
                    if TicTacToe.turn:
                        screen.blit(o, (200, 100))
                        pygame.display.flip()
                        pygame.display.update()
                    else:
                        screen.blit(x, (200, 100))
                        pygame.display.flip()
                        pygame.display.update()
            elif mouse_position[0] <= 100 and 100 <= mouse_position[1] <= 200:
                if TicTacToe.move('middle-left'):
                    TicTacToe.display_board()
                    TicTacToe.alternate_turn()
                    if TicTacToe.turn:
                        screen.blit(o, (0, 100))
                        pygame.display.flip()
                        pygame.display.update()
                    else:
                        screen.blit(x, (0, 100))
                        pygame.display.flip()
                        pygame.display.update()
            elif mouse_position[0] <= 100 and 200 <= mouse_position[1] <= 300:
                if TicTacToe.move('bottom-left'):
                    TicTacToe.display_board()
                    TicTacToe.alternate_turn()
                    if TicTacToe.turn:
                        screen.blit(o, (0, 200))
                        pygame.display.flip()
                        pygame.display.update()
                    else:
                        screen.blit(x, (0, 200))
                        pygame.display.flip()
                        pygame.display.update()
            elif 100 <= mouse_position[0] <= 200 and 200 <= mouse_position[1] <= 300:
                if TicTacToe.move('bottom-center'):
                    TicTacToe.display_board()
                    TicTacToe.alternate_turn()
                    if TicTacToe.turn:
                        screen.blit(o, (100, 200))
                        pygame.display.flip()
                        pygame.display.update()
                    else:
                        screen.blit(x, (100, 200))
                        pygame.display.flip()
                        pygame.display.update()
            elif 200 <= mouse_position[0] <= 300 and 200 <= mouse_position[1] <= 300:
                if TicTacToe.move('bottom-right'):
                    TicTacToe.display_board()
                    TicTacToe.alternate_turn()
                    if TicTacToe.turn:
                        screen.blit(o, (200, 200))
                        pygame.display.flip()
                        pygame.display.update()
                    else:
                        screen.blit(x, (200, 200))
                        pygame.display.flip()
                        pygame.display.update()
    if TicTacToe.check_for_three():
        if TicTacToe.turn:
            caption = "O Wins!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        else:
            caption = "X Wins!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        pygame.display.set_caption(caption)
        time.sleep(10)
        exit()
    # screen.blit(x, (100,100))
    # screen.blit(o, (0, 0))
    pygame.display.flip()
    pygame.time.Clock().tick(240)
