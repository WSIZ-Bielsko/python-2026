

def sum_and_avg(data: list[float]) -> tuple[float,float]:
    """
    returns sum and average of the `data`
    :param data:
    :return:
    """
    sum_data = sum(data)
    return sum_data, sum_data/len(data)
