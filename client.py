class SpaNetworkIdleSettlementWaiterClient:
    def await_dom_settlement(self, page_url='https://app.dashboard.com/analytics', max_wait_ms=5000, pending_xhr_threshold=0):
        return {
            'wait_session_id': 'spa_idl_5519',
            'page_url': page_url,
            'network_idle_achieved': True,
            'settlement_time_ms': 640,
            'dom_mutations_quiescent': True,
            'hydration_complete': True,
            'telemetry_trace_url': 'https://tabbit.settlement.genpark.ai/traces/5519.json'
        }
