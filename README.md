*advancing-hero2 - Projeto de CES29*
============================================
Continuação do projeto knight_of_valhalla

**Grupo**
1. *Éric Bastos*
2. *Enzo Vargas*
3. *Due Jie Wan*
4. *Mateus Nobre*
5. *Lucas Inamine*
6. *Thomas Castro*
-----------------------
![GifJogo](./advancing_hero/images/readme_images/knight_of_valhalla_gif.gif)

Cuidado ao adicionar arquivos ao repositório.
---------------------------------------------

NÃO USE GIT ADD ., GIT COMMIT -A, etc.
--------------------------------------

Dê um git add em cada arquivo (se tiver vários use git add -i). Isso vai evitar que o repositório fique cheio de lixo. 
Lembre que não tem como apagar o lixo do repositório, ele sempre vai ficar no histórico, então enviar binários por 
exemplo é estritamente proibido.


## Instalando as dependências

- Rode no seu terminal, dentro da pasta main, `python setup.py install`
- Caso não tenha  setuptools, execute o comando `sudo apt-get install -y python-setuptools`

>**Observação:** Dependendo da máquina, nas instruções acima ,deve-se utilizar o comando `python3` no lugar de `python`. Para descobrir qual o comando correto, digite no terminal  `which python` e veja se há um arquivo `bin` que corresponde ao comando. Caso não haja, tente com `which python3` e certifique-se que existe este arquivo.

## Iniciando o jogo

- Para iniciar o jogo, basta executar, estando na pasta da main, o comando `python advancing_hero`

## Instruções para uma boa experiência

- Com o jogo iniciado, o jogador se encontrará na tela de início, podendo tanto iniciar o jogo (**Play Game**), como sair (**Exit Game**):
  ![TelaInicio](./advancing_hero/images/readme_images/TelaInicio.png)

> Os comandos para selecionar podem ser feitos utilizando as teclas **PgUp/W** e **PgDn/S** do teclado. Para clicar basta utilizar as teclas **Space/Enter**.

 - Dentro do jogo, os comandos necessários para ter uma experiência agradável, é necessário ter em mente os seguintes comandos:
  ![Gameplay](./advancing_hero/images/readme_images/Gameplay.png)
  > - Para *movimentar* o personagem, utilizamos as teclas:
  >    - **W**: Movimentar para cima
  >    - **A**: Movimentar para a esquerda
  >    - **S**: Movimentar para baixo
  >    - **D**: Movimentar para a direita
  > - Para *atacar* os inimigos, utilizam-se as teclas:
  >    - **PgUp + Espaço**: Lança o bumerangue
  >    - **PgDn + Espaço**: Lança flexas

> **Disclaimer:** Vale a pena notar que o nosso personagem, Ragnar, se movimenta em velocidades diferentes dependendo do ambiente em que pisa. Pode-se notar este fato observando que na água ele se move com maior dificuldade.
- Quando o personagem fica sem "vida" suficiente, o jogo acaba e fica-se com a tela de "Game Over":
![GameOver](./advancing_hero/images/readme_images/GameOver.png)
- Se desejar reiniciar um outro jogo, basta utilizar qualquer tecla que irá redicionar para a tecla inicial.

## Referências 
- Efeitos Sonoros retirados de: 
    https://freesound.org/people/4barrelcarb/sounds/365378/ .

- Sprites e Gráficos retirados de:
-   https://kenney.nl/assets/roguelike-caves-dungeons ;
-   https://kenney.nl/assets/rpg-base; e
-   https://www.spriters-resource.com/ .
