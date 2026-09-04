from client import SpaNetworkIdleSettlementWaiterClient

def main():
    client = SpaNetworkIdleSettlementWaiterClient()
    res = client.await_dom_settlement()
    print('SPA Idle Waiter: ' + res['wait_session_id'] + ' (Settled: ' + str(res['network_idle_achieved']) + ')')
    print('Duration: ' + str(res['settlement_time_ms']) + 'ms | Hydration Complete: ' + str(res['hydration_complete']))
    print('Trace URL: ' + res['telemetry_trace_url'])

if __name__ == '__main__':
    main()
