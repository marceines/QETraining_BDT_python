Feature: Customer search
outline to simulate a search of a total price for a list clients
  
  Scenario Outline: Customer search of a total price for a list clients
    Given I have <Name> for my user
	And I have <ClientId> for my client
	When I Search <ClientId> in the list
	Then I should receive <Total> price of purchase for client
	

 Examples:
 |ClientId	|Name	   |Total 	|
 |10 	  	|Ronny     |$100		|
 |20 	  	|Irina     |$200 	|
 |30 	  	|Ines      |$300 	|
 |40 	  	|Tania     |$400 	|

