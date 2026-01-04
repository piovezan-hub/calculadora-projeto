#!/bin/bash
echo "--- Calculadora Bash ---"
read -p "Digite o primeiro numero: " num1
read -p "Digite o segundo numero: " num2
resultado=$((num1 + num2))
echo "O resultado da soma é: $resultado"
