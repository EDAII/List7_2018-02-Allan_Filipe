from django.shortcuts import render
# from datetime import datetime
# import time

# Coins list used in coin changing greed algorithm
coins_list = [1, 5, 10, 25, 50, 100]


def home(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.POST['selectedOption']:
        myfile = request.FILES['myfile']
        byte_str = myfile.file.read()

        # Convert to a "unicode" object
        text_obj = byte_str.decode('UTF-8')

        # Choosing algorithm options
        if request.POST['selectedOption'] == "Knapsack":
            columns_descriptions, values, weights, limit = read_csv_knapsack(text_obj.splitlines())
            values_quantit = len(values)
            data = []
            for number in range(0, values_quantit):
                data.append([values[number], weights[number]])

            weights_list = []
            for weight in range(0, limit+1):
                weights_list.append(weight)

            result, table = knapSack(limit, weights, values, values_quantit)
            items = getItems(table, limit, values_quantit, weights, values)

            return render(request, 'result.html', {'algorithm': request.POST['selectedOption'],
                                                   'columns_descriptions': columns_descriptions,
                                                   'values_quantit': values_quantit,
                                                   'weights_list': weights_list,
                                                   'limit': limit,
                                                   'result': result,
                                                   'table': table,
                                                   'items':items,
                                                   'data': data})
        '''
        elif request.POST['selectedOption'] == "Greed - Interval Scheduling":
            columns_descriptions, all_data = read_csv_jobs(text_obj.splitlines())

            jobs_list = sorted(all_data, key=getKey)

            jobs_list = convert_to_datetime(jobs_list)

            jobs_selected, execution_time = interval_scheduling_jobs(jobs_list)

            return render(request, 'result.html', {'algorithm': request.POST['selectedOption'],
                                                   'columns_descriptions': columns_descriptions,
                                                   'jobs_list': jobs_list,
                                                   'jobs_selected': jobs_selected,
                                                   'execution_time': execution_time})
        
        else:
            # Nothing to do
            pass
        '''
    else:
        # Nothing to do
        pass

    return render(request, 'home.html')


def read_csv_knapsack(file):
    values = []
    weights = []
    limit = []
    columns_descriptions = []

    # Save all csv data in a list of lists, removing '\n' at the last line element.
    for line in file:
        if not columns_descriptions:
            columns_descriptions = line.split(",")
            columns_descriptions[-1] = columns_descriptions[-1].strip("\n")
        else:
            data = line.split(",")
            values.append(int(data[0]))
            weights.append(int(data[1]))
            limit.append(int(data[2]))

    return columns_descriptions, values, weights, limit[0]


def getItems(values_table, weight_limit, values_quantit, weights, values):
    result = values_table[values_quantit][weight_limit]
    items = []

    for number in range(values_quantit, 0, -1):
        if result <= 0:
            break
        if result == values_table[number - 1][weight_limit]:
            continue
        else:
            items.append(weights[number - 1])

            result = result - values[number - 1]
            weight_limit = weight_limit - weights[number - 1]

    return items


def knapSack(weight_limit, weights, values, values_quantit): 
    values_table = [[0 for x in range(weight_limit+1)] for x in range(values_quantit+1)] 

    for item in range(values_quantit+1): 
        for weight in range(weight_limit+1): 
            if item == 0 or weight == 0: 
                values_table[item][weight] = 0
            elif weights[item-1] <= weight: 
                values_table[item][weight] = max(values[item-1] + values_table[item-1][weight-weights[item-1]], values_table[item-1][weight]) 
            else: 
                values_table[item][weight] = values_table[item-1][weight] 

    return values_table[values_quantit][weight_limit], values_table 
