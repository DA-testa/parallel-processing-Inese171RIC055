def parallel_processing(n, m, data):
    output = []

    # Initialize threads and finish times
    threads = [0] * n
    finish_times = [0] * n
    
    # Process the jobs
    for i in range(m):
        job_time = data[i]
        
        # Choose the earliest available thread
        min_finish_time = min(finish_times)
        thread_index = finish_times.index(min_finish_time)
        
        # Update the thread's finish time
        start_time = max(threads[thread_index], finish_times[thread_index])
        finish_times[thread_index] = start_time + job_time
        threads[thread_index] = start_time
        
        # Add the job details to the output
        output.append((thread_index, start_time))
    
    return output


def main():
    # Read input
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # Call the parallel_processing function
    result = parallel_processing(n, m, data)
    
    # Print the output
    for pair in result:
        print(pair[0], pair[1])


if __name__ == "__main__":
    main()