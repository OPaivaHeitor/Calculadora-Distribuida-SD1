﻿# Calculadora-Distribuida-SD1

## Atividade proposta
Implemente uma calculadora distribuída que permita um cliente consultar serviços de operações aritméticas básicas tais como: somar, subtrair, multiplicar ou dividir. A quantidade de números a serem somados, subtraídos ou multiplicados está limitado a 20 números. Os números de entrada estão na mesma linha separador por um espaço. Ao teclar ENTER, o serviço correspondente da calculadora deve ser invocado.

O servidor da calculadora distribuída deve atender requisições na porta 15000 usando o protocolo TCP. O cliente deve oferecer um menu para o usuário escolher qual operação deseja executar. Após escolher uma operação aritmética, o usuário deve informar os números desejados, conectar no servidor, aguardar resposta e imprimir o resultado na tela.

O menu de operações aritméticas deverá ser apresentado novamente para o usuário escolher outra operação ou encerrar o programa.

## Realização
Foram abertas duas máquinas virtuais no sistema da AWS Academy, uma para o ```Servidor``` e uma para o ```Cliente```

 Para o vínculo do ```Cliente``` e ```Servidor``` foi usado o IP de coneção do Servidor

### Rodando o Código
Ao executar o ```Cliente``` no terminal da maquina da AWS, aparece o menu de interação para a solicitação dos valores e da operação a ser realizada.

É passada uma String com as informações para o servidor que vai particionar a String e identificar a operação e os valores.

É feito o print no terminal do ```Servidor``` para a verificação e retornado o valor ao ```Cliente``` aparecendo o resultado no terminal.
