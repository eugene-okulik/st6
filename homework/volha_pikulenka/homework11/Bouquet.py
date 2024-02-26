class Bouquet:
    def __init__(self, flower_names:str, flower_prices:int,
                flower_colors: str, avr_lifetime_in_days:int):
        self.flower_names = flower_names
        self.flower_prices = flower_prices
        self.flower_colors = flower_colors
        self.avr_lifetime_in_days = avr_lifetime_in_days
        self.bouquet_info = self.zipping()
   
    def zipping(self):
        return (list(zip(self.flower_names, self.flower_prices,
                        self.flower_colors,self.avr_lifetime_in_days)))
    
    def bouquet_price(self):
        total_price = 0
        for price in self.flower_prices:
            total_price = total_price + price
        print(f'Bouquet price: {str(total_price // len(self.flower_prices))}')

    def bouquet_avr_lifetime_in_days(self):
        total_lifetime = 0
        for lifetime in self.avr_lifetime_in_days:
            total_lifetime = total_lifetime + lifetime
        print(f'Average lifetime is {str(total_lifetime//len(self.avr_lifetime_in_days))} days')

    def sort_by_name(self, acs_desc='acs'):
        if acs_desc == 'acs':
            print('Sorted by name ASC', sep='\n')
            return print(sorted(self.bouquet_info, key=lambda x: x[0]))
        elif acs_desc == 'desc':
            print('Sorted by name DESC', sep='\n')
            return print(sorted(self.bouquet_info, key=lambda x: x[0],reverse=True))
    
    def sort_by_price(self, acs_desc='acs'):
        if acs_desc == 'acs':
            print('Sorted by price ASC', sep='\n')
            return print(sorted(self.bouquet_info, key=lambda x: x[1]))
        elif acs_desc == 'desc':
            print('Sorted by price DESC', sep='\n')
            return print(sorted(self.bouquet_info, key=lambda x: x[1],reverse=True))

    def sort_by_color(self, acs_desc='acs'):
        if acs_desc == 'acs':
            print('Sorted by color ASC', sep='\n')
            return print(sorted(self.bouquet_info, key=lambda x: x[2]))
        elif acs_desc == 'desc':
            print('Sorted by color DESC', sep='\n')
            return print(sorted(self.bouquet_info, key=lambda x: x[2],reverse=True))
        
    def sort_by_freshness(self, acs_desc='acs'):
        if acs_desc == 'acs':
            print('Sorted by freshness ASC', sep='\n')
            return print(sorted(self.bouquet_info, key=lambda x: x[3]))
        elif acs_desc == 'desc':
            print('Sorted by freshness DESC', sep='\n')
            return print(sorted(self.bouquet_info, key=lambda x: x[3],reverse=True))
   
    def search_name_based_on_lifetime(self, lifetime_days):
            for lifetime in self.avr_lifetime_in_days:
                if lifetime == lifetime_days:
                    i = self.avr_lifetime_in_days.index(lifetime)
                    return print(f'{self.flower_names[i].title()} '
                                f'has lifetime {lifetime_days} days')
            return print('Nothing was found')


bouquet1 = Bouquet(['rose', 'daisy', 'springs'], [50, 44, 68],
                   ['red', 'yellow', 'blue'], [11, 12, 15])

bouquet2 = Bouquet(['dundelion', 'daffodils', 'astras'], [30, 11, 8],
                   ['yellow-bright', 'white', 'purple'], [8, 13, 5])

print(bouquet1.bouquet_info)
# bouquet1.bouquet_price()
# bouquet1.bouquet_avr_lifetime_in_days()
# bouquet1.sort_by_name()
# bouquet1.sort_by_color()
# bouquet1.sort_by_freshness('desc')
# bouquet1.search_name_based_on_lifetime(12)
