def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    ticket_cost=0
    rate_per_adult=37550
    rate_per_child=1/3(rate_per_adult)
    ticket_cost=rate_per_adult+rate_per_child
    service_tax=7/100(ticket_cost)
    final_ticket=ticket_cost+service_tax
    discount=(10/100)*final_ticket
    total_ticket_cost=final_ticket-discount
    return total_ticket_cost
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)
