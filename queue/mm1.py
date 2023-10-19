rng = np.random.default_rng()

inter_arrival_time_d = rng.poisson(5,449)
arrival_time_d = []
start = 0
for i in range(0,len(inter_arrival_time_d)):
  start += inter_arrival_time_d[i]
  arrival_time_d.append(start)

service_time_d = int(rng.exponential(4,1))
customer_wait_time_d = 0
system_idle_time_d = arrival_time_d[0]
system_idle_count_d = 1

service_start_d = []
service_start_d.append(arrival_time_d[0])
for i in range(1,len(inter_arrival_time_d)):

  service_start_d.append(max(service_time_d+service_start_d[i-1],arrival_time_d[i]))

  if service_time_d+service_start_d[i-1] > arrival_time_d[i]:
    customer_wait_time_d += service_time_d+service_start_d[i-1] - arrival_time_d[i]

  elif service_time_d+service_start_d[i-1] < arrival_time_d[i]:
    system_idle_count_d+=1
    system_idle_time_d = arrival_time_d[i] - service_time_d+service_start_d[i-1]
