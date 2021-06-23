import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-orders',
  templateUrl: './orders.component.html',
  styleUrls: ['./orders.component.css']
})
export class OrdersComponent implements OnInit {
  ordersData = [{
    "name": "Delinda",
    "status": "ready",
    "items": [
      {
        "name": "Wine - Niagara,vqa Reisling",
        "price": 13.6
      },
      {
        "name": "Flour - Teff",
        "price": 20.17
      },
      {
        "name": "Apples - Spartan",
        "price": 48.96
      }
    ]
  }, {
    "name": "Etheline",
    "status": "delivering",
    "items": [
      {
        "name": "Chicken - Base",
        "price": 46.69
      },
      {
        "name": "Beef - Texas Style Burger",
        "price": 17.54
      },
      {
        "name": "Juice - Tomato, 10 Oz",
        "price": 35.41
      }
    ]
  }, {
    "name": "Zandra",
    "status": "preparation",
    "items": [
      {
        "name": "Cleaner - Bleach",
        "price": 42.66
      },
      {
        "name": "Soup Campbells Mexicali Tortilla",
        "price": 46.55
      },
      {
        "name": "Soup - Campbells, Spinach Crm",
        "price": 24.73
      }
    ]
  }, {
    "name": "Zia",
    "status": "delivering",
    "items": [
      {
        "name": "Cheese - Cheddar, Mild",
        "price": 23.68
      }
    ]
  }, {
    "name": "Skip",
    "status": "delivering",
    "items": [
      {
        "name": "Lotus Root",
        "price": 15.06
      }
    ]
  }, {
    "name": "Cynde",
    "status": "delivering",
    "items": [
      {
        "name": "Bread - Dark Rye, Loaf",
        "price": 17.76
      }
    ]
  }, {
    "name": "Tabb",
    "status": "delivering",
    "items": [
      {
        "name": "Tendrils - Baby Pea, Organic",
        "price": 42.71
      }
    ]
  }, {
    "name": "Cristen",
    "status": "preparation",
    "items": [
      {
        "name": "Cinnamon - Ground",
        "price": 30.73
      }
    ]
  }, {
    "name": "Cyrille",
    "status": "delivering",
    "items": [
      {
        "name": "Cake - Dulce De Leche",
        "price": 20.2
      }
    ]
  }, {
    "name": "Kiele",
    "status": "ready",
    "items": [
      {
        "name": "Pork - Butt, Boneless",
        "price": 48.69
      }
    ]
  }, {
    "name": "Lonee",
    "status": "preparation",
    "items": [
      {
        "name": "Ham - Virginia",
        "price": 36.28
      },
      {
        "name": "Island Oasis - Ice Cream Mix",
        "price": 52.67
      },
      {
        "name": "Pepper Squash",
        "price": 32.98
      }
    ]
  }, {
    "name": "Stoddard",
    "status": "preparation",
    "items": [
      {
        "name": "Oil - Olive Bertolli",
        "price": 42.22
      }
    ]
  }, {
    "name": "Portie",
    "status": "beforPayment",
    "items": [
      {
        "name": "Strawberries",
        "price": 51.63
      },
      {
        "name": "Bread - Pumpernickle, Rounds",
        "price": 57.21
      }
    ]
  }, {
    "name": "Anselma",
    "status": "beforPayment",
    "items": [
      {
        "name": "Sword Pick Asst",
        "price": 29.91
      },
      {
        "name": "Oyster - In Shell",
        "price": 34.43
      },
      {
        "name": "Tray - Foam, Square 4 - S",
        "price": 24.43
      }
    ]
  }, {
    "name": "Irwin",
    "status": "delivering",
    "items": [
      {
        "name": "Crackers - Water",
        "price": 16.38
      }
    ]
  }, {
    "name": "Chrystel",
    "status": "ready",
    "items": [
      {
        "name": "Wine - Jaboulet Cotes Du Rhone",
        "price": 11.43
      },
      {
        "name": "Tamarillo",
        "price": 52.53
      },
      {
        "name": "Lobster - Tail 6 Oz",
        "price": 54.41
      }
    ]
  }, {
    "name": "Meredeth",
    "status": "beforPayment",
    "items": [
      {
        "name": "Wine - Pinot Noir Pond Haddock",
        "price": 18.26
      },
      {
        "name": "Pastry - Plain Baked Croissant",
        "price": 20.11
      },
      {
        "name": "Syrup - Pancake",
        "price": 54.66
      }
    ]
  }, {
    "name": "Correy",
    "status": "ready",
    "items": [
      {
        "name": "Huck White Towels",
        "price": 38.75
      },
      {
        "name": "Syrup - Monin - Blue Curacao",
        "price": 25.6
      },
      {
        "name": "Lamb - Whole, Fresh",
        "price": 53.07
      }
    ]
  }, {
    "name": "Rene",
    "status": "finish",
    "items": [
      {
        "name": "Fiddlehead - Frozen",
        "price": 47.15
      }
    ]
  }, {
    "name": "Upton",
    "status": "delivering",
    "items": [
      {
        "name": "Vodka - Smirnoff",
        "price": 43.49
      }
    ]
  }, {
    "name": "Angelico",
    "status": "beforPayment",
    "items": [
      {
        "name": "Milk 2% 500 Ml",
        "price": 20.9
      },
      {
        "name": "Ecolab - Hand Soap Form Antibac",
        "price": 52.4
      },
      {
        "name": "Flower - Commercial Bronze",
        "price": 25.37
      }
    ]
  }, {
    "name": "Chaddy",
    "status": "finish",
    "items": [
      {
        "name": "Wine - Red, Marechal Foch",
        "price": 49.04
      }
    ]
  }, {
    "name": "Arther",
    "status": "ready",
    "items": [
      {
        "name": "Muffin - Mix - Mango Sour Cherry",
        "price": 47.48
      }
    ]
  }, {
    "name": "Katya",
    "status": "preparation",
    "items": [
      {
        "name": "V8 Splash Strawberry Kiwi",
        "price": 28.57
      },
      {
        "name": "Chinese Foods - Plain Fried Rice",
        "price": 42.33
      }
    ]
  }, {
    "name": "James",
    "status": "finish",
    "items": [
      {
        "name": "Onions Granulated",
        "price": 45.49
      }
    ]
  }, {
    "name": "Conway",
    "status": "finish",
    "items": [
      {
        "name": "Shrimp - Black Tiger 26/30",
        "price": 29.78
      },
      {
        "name": "Rum - White, Gg White",
        "price": 38.52
      },
      {
        "name": "Energy Drink - Franks Original",
        "price": 52.91
      }
    ]
  }, {
    "name": "Monah",
    "status": "beforPayment",
    "items": [
      {
        "name": "Papayas",
        "price": 10.74
      }
    ]
  }, {
    "name": "Audi",
    "status": "preparation",
    "items": [
      {
        "name": "Chinese Foods - Pepper Beef",
        "price": 54.36
      }
    ]
  }, {
    "name": "Doris",
    "status": "delivering",
    "items": [
      {
        "name": "Toamtoes 6x7 Select",
        "price": 54.16
      },
      {
        "name": "Haggis",
        "price": 38.75
      },
      {
        "name": "Green Tea Refresher",
        "price": 28.1
      }
    ]
  }, {
    "name": "Rudie",
    "status": "ready",
    "items": [
      {
        "name": "Apple - Fuji",
        "price": 36.86
      },
      {
        "name": "Wine - Cava Aria Estate Brut",
        "price": 59.16
      }
    ]
  }, {
    "name": "Lenette",
    "status": "beforPayment",
    "items": [
      {
        "name": "Longos - Grilled Veg Sandwiches",
        "price": 29.81
      },
      {
        "name": "Paper Cocktail Umberlla 80 - 180",
        "price": 17.66
      },
      {
        "name": "Coffee - Almond Amaretto",
        "price": 49.39
      }
    ]
  }, {
    "name": "Fanchon",
    "status": "preparation",
    "items": [
      {
        "name": "Ginsing - Fresh",
        "price": 44.67
      }
    ]
  }, {
    "name": "Blake",
    "status": "preparation",
    "items": [
      {
        "name": "Nantucket - Pomegranate Pear",
        "price": 32.44
      }
    ]
  }, {
    "name": "Dorene",
    "status": "beforPayment",
    "items": [
      {
        "name": "Onions - Cippolini",
        "price": 19.39
      },
      {
        "name": "Pasta - Angel Hair",
        "price": 22.7
      },
      {
        "name": "Thyme - Dried",
        "price": 58.22
      }
    ]
  }, {
    "name": "Tulley",
    "status": "ready",
    "items": [
      {
        "name": "Kaffir Lime Leaves",
        "price": 41.27
      },
      {
        "name": "Bread - Frozen Basket Variety",
        "price": 10.58
      }
    ]
  }, {
    "name": "Kip",
    "status": "delivering",
    "items": [
      {
        "name": "Scallop - St. Jaques",
        "price": 47.84
      }
    ]
  }, {
    "name": "Alys",
    "status": "ready",
    "items": [
      {
        "name": "Food Colouring - Blue",
        "price": 45.39
      },
      {
        "name": "Beef Dry Aged Tenderloin Aaa",
        "price": 45.43
      }
    ]
  }, {
    "name": "Caresa",
    "status": "finish",
    "items": [
      {
        "name": "Cream - 10%",
        "price": 16.23
      },
      {
        "name": "Soup - Tomato Mush. Florentine",
        "price": 16.46
      }
    ]
  }, {
    "name": "Roxi",
    "status": "delivering",
    "items": [
      {
        "name": "Wine - Chardonnay South",
        "price": 33.43
      },
      {
        "name": "Pur Value",
        "price": 42.63
      }
    ]
  }, {
    "name": "Cozmo",
    "status": "ready",
    "items": [
      {
        "name": "Oil - Olive, Extra Virgin",
        "price": 42.49
      },
      {
        "name": "Beef - Tenderloin Tails",
        "price": 58.31
      }
    ]
  }, {
    "name": "Barton",
    "status": "finish",
    "items": [
      {
        "name": "Cheese - Ricotta",
        "price": 50.95
      },
      {
        "name": "Blueberries - Frozen",
        "price": 9.31
      }
    ]
  }, {
    "name": "Salvatore",
    "status": "delivering",
    "items": [
      {
        "name": "Tart - Pecan Butter Squares",
        "price": 20.27
      }
    ]
  }, {
    "name": "Kristoffer",
    "status": "preparation",
    "items": [
      {
        "name": "Water Chestnut - Canned",
        "price": 31.37
      },
      {
        "name": "Neckerchief Blck",
        "price": 32.64
      }
    ]
  }, {
    "name": "Roseann",
    "status": "delivering",
    "items": [
      {
        "name": "Cocoa Feuilletine",
        "price": 5.9
      },
      {
        "name": "Longos - Burritos",
        "price": 28.29
      },
      {
        "name": "Juice - Lemon",
        "price": 49.25
      }
    ]
  }, {
    "name": "Happy",
    "status": "delivering",
    "items": [
      {
        "name": "Hersey Shakes",
        "price": 7.98
      },
      {
        "name": "Lobak",
        "price": 30.49
      }
    ]
  }, {
    "name": "Cosetta",
    "status": "ready",
    "items": [
      {
        "name": "Guinea Fowl",
        "price": 52.29
      },
      {
        "name": "Veal - Inside, Choice",
        "price": 41.55
      }
    ]
  }, {
    "name": "Floria",
    "status": "ready",
    "items": [
      {
        "name": "Lettuce - California Mix",
        "price": 40.76
      }
    ]
  }, {
    "name": "Irvine",
    "status": "preparation",
    "items": [
      {
        "name": "Jam - Raspberry,jar",
        "price": 54.21
      }
    ]
  }, {
    "name": "Timothee",
    "status": "preparation",
    "items": [
      {
        "name": "Muffin Batt - Ban Dream Zero",
        "price": 36.36
      }
    ]
  }, {
    "name": "Meghan",
    "status": "ready",
    "items": [
      {
        "name": "Wine - Niagara Peninsula Vqa",
        "price": 46.1
      },
      {
        "name": "Goldschalger",
        "price": 26.38
      }
    ]
  }];
  constructor() { }

  ngOnInit(): void {
  }

}
