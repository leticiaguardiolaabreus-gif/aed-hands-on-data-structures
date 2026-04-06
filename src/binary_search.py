from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    """
    Realiza busca binária em um array ordenado.

    Deve retornar o índice do elemento ou -1 caso não encontrado.
    """
    primeiro = 0
    ultimo = len(array)-1

    while primeiro <= ultimo:
        meio = ((primeiro + ultimo)//2)
        valor_atual = array.get(meio)

        if valor_atual == target:
            return meio

        if target > valor_atual:
            primeiro = meio +1

        if target < valor_atual:
            ultimo = meio -1

    return -1




    raise NotImplementedError
