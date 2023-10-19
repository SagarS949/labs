def Calculate_Waiting_time_two_server(flag):
  if flag == "Random":
    Service_time=3
  else:
    Service_times=np.random.exponential(4,1)
    Service_time = Service_times[0]
    print(Service_time)
  Arriving_time_2_servers = Calculate_Arrival(flag)
  server1_waiting_time=Arriving_time_2_servers[0]
  server2_waiting_time=0
  server1_end_time = Arriving_time_2_servers[0] + Service_time
  server2_end_time = 0
  customer_waiting = 0

  for i in range(1,len(Arriving_time_2_servers)):

    if server1_end_time > server2_end_time:
      server2_waiting_time =   server2_waiting_time + (Arriving_time_2_servers[i] - server2_end_time)
      server2_end_time = Arriving_time_2_servers[i] + Service_time
      if server2_end_time > Arriving_time_2_servers[i]:
        customer_waiting = customer_waiting + (server2_end_time - Arriving_time_2_servers[i])

    else:
      server1_waiting_time =  server1_waiting_time + (Arriving_time_2_servers[i] - server1_end_time)
      server1_end_time = Arriving_time_2_servers[i] + Service_time
      if server1_end_time > Arriving_time_2_servers[i]:
        customer_waiting = customer_waiting + (server1_end_time - Arriving_time_2_servers[i])

  print("Server 1 waits for ",server1_waiting_time," minutes")
  print("Server 1 waits on an average for ",server1_waiting_time/450," minutes")
  print("Server 2 waits for ",server2_waiting_time," minutes")
  print("Server 2 waits on an average for ",server2_waiting_time/450," minutes")
  print("The overall customer waiting time is ",customer_waiting," minutes")
  print("The average customer waiting time is ",customer_waiting/450," minutes")
