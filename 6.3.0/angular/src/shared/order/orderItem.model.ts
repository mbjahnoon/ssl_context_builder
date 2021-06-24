export class OrderItem {
    id?: string;
    customerName?: string;
    status?: string;
    items?: object[];
    sum?: number;
    statusesTimestamp? : [];
    constructor(
    ) {
    }
  };

  export var MockOrdersItems:OrderItem[] = [{
    "customerName": "Louisette",
    "status": "beforPayment",
    "items": [
      {
        "name": "Bacardi Breezer - Strawberry",
        "price": 34.17
      },
      {
        "name": "Sugar - Cubes",
        "price": 20.87
      },
      {
        "name": "Crab - Claws, 26 - 30",
        "price": 57.62
      }
    ]
  }, {
    "customerName": "Charmion",
    "status": "preparation",
    "items": [
      {
        "name": "Potatoes - Fingerling 4 Oz",
        "price": 40.85
      },
      {
        "name": "Brandy Cherry - Mcguinness",
        "price": 53.24
      }
    ]
  }, {
    "customerName": "Cord",
    "status": "delivering",
    "items": [
      {
        "name": "Pastry - Baked Scones - Mini",
        "price": 42.13
      }
    ]
  }, {
    "customerName": "Verna",
    "status": "finish",
    "items": [
      {
        "name": "Gherkin",
        "price": 6.54
      },
      {
        "name": "Water, Tap",
        "price": 52.3
      },
      {
        "name": "Muffin Batt - Ban Dream Zero",
        "price": 30.1
      }
    ]
  }, {
    "customerName": "Clay",
    "status": "preparation",
    "items": [
      {
        "name": "Kiwi Gold Zespri",
        "price": 29.68
      }
    ]
  }, {
    "customerName": "Lemar",
    "status": "beforPayment",
    "items": [
      {
        "name": "V8 Splash Strawberry Kiwi",
        "price": 16.27
      },
      {
        "name": "Kellogs Cereal In A Cup",
        "price": 28.17
      }
    ]
  }, {
    "customerName": "Rosalinde",
    "status": "delivering",
    "items": [
      {
        "name": "Chevril",
        "price": 50.41
      },
      {
        "name": "Shrimp - 16 - 20 Cooked, Peeled",
        "price": 34.39
      },
      {
        "name": "Wine - Red, Gamay Noir",
        "price": 23.13
      }
    ]
  }, {
    "customerName": "Eadie",
    "status": "preparation",
    "items": [
      {
        "name": "Basil - Seedlings Cookstown",
        "price": 33.77
      },
      {
        "name": "Creme De Banane - Marie",
        "price": 20.28
      }
    ]
  }, {
    "customerName": "Shadow",
    "status": "ready",
    "items": [
      {
        "name": "Brandy Apricot",
        "price": 41.93
      },
      {
        "name": "Wine - Zinfandel California 2002",
        "price": 13.07
      }
    ]
  }, {
    "customerName": "Miltie",
    "status": "preparation",
    "items": [
      {
        "name": "Wine - Ruffino Chianti",
        "price": 56.21
      },
      {
        "name": "Ecolab Digiclean Mild Fm",
        "price": 47.7
      }
    ]
  }, {
    "customerName": "Chase",
    "status": "finish",
    "items": [
      {
        "name": "Dried Peach",
        "price": 22.58
      }
    ]
  }, {
    "customerName": "Ramsey",
    "status": "ready",
    "items": [
      {
        "name": "Pasta - Fettuccine, Dry",
        "price": 41.91
      },
      {
        "name": "Cookies - Assorted",
        "price": 52.65
      },
      {
        "name": "Shrimp - Black Tiger 26/30",
        "price": 38.42
      }
    ]
  }, {
    "customerName": "Josephine",
    "status": "beforPayment",
    "items": [
      {
        "name": "Vinegar - Rice",
        "price": 49.13
      },
      {
        "name": "Pie Filling - Pumpkin",
        "price": 53.85
      }
    ]
  }, {
    "customerName": "Loydie",
    "status": "delivering",
    "items": [
      {
        "name": "Coffee - Colombian, Portioned",
        "price": 51.77
      },
      {
        "name": "Yogurt - French Vanilla",
        "price": 20.75
      }
    ]
  }, {
    "customerName": "Elle",
    "status": "ready",
    "items": [
      {
        "name": "Beans - Kidney, Canned",
        "price": 19.65
      }
    ]
  }, {
    "customerName": "Rosalie",
    "status": "ready",
    "items": [
      {
        "name": "Lumpfish Black",
        "price": 13.18
      }
    ]
  }, {
    "customerName": "Seka",
    "status": "delivering",
    "items": [
      {
        "name": "Soup - Chicken And Wild Rice",
        "price": 14.0
      },
      {
        "name": "Bread - Mini Hamburger Bun",
        "price": 55.01
      },
      {
        "name": "Foil Cont Round",
        "price": 57.81
      }
    ]
  }, {
    "customerName": "Bartholemy",
    "status": "finish",
    "items": [
      {
        "name": "Devonshire Cream",
        "price": 42.21
      }
    ]
  }, {
    "customerName": "Chase",
    "status": "preparation",
    "items": [
      {
        "name": "Oil - Shortening - All - Purpose",
        "price": 40.53
      }
    ]
  }, {
    "customerName": "Jennica",
    "status": "ready",
    "items": [
      {
        "name": "Bacon Strip Precooked",
        "price": 33.16
      },
      {
        "name": "Turkey - Whole, Fresh",
        "price": 41.73
      }
    ]
  }, {
    "customerName": "Shani",
    "status": "delivering",
    "items": [
      {
        "name": "Mace",
        "price": 29.02
      },
      {
        "name": "Beer - Original Organic Lager",
        "price": 44.63
      },
      {
        "name": "Parsley Italian - Fresh",
        "price": 55.53
      }
    ]
  }, {
    "customerName": "Stephannie",
    "status": "finish",
    "items": [
      {
        "name": "Cassis",
        "price": 40.53
      },
      {
        "name": "Tumeric",
        "price": 46.47
      },
      {
        "name": "Chicken Giblets",
        "price": 41.26
      }
    ]
  }, {
    "customerName": "Sonia",
    "status": "ready",
    "items": [
      {
        "name": "Rabbit - Frozen",
        "price": 52.7
      },
      {
        "name": "Mushroom - Enoki, Fresh",
        "price": 17.7
      },
      {
        "name": "Sugar - Cubes",
        "price": 41.65
      }
    ]
  }, {
    "customerName": "Annadiana",
    "status": "preparation",
    "items": [
      {
        "name": "Pails With Lids",
        "price": 12.55
      }
    ]
  }, {
    "customerName": "Bren",
    "status": "delivering",
    "items": [
      {
        "name": "Wine - Ej Gallo Sonoma",
        "price": 20.16
      },
      {
        "name": "Wine - Masi Valpolocell",
        "price": 19.38
      },
      {
        "name": "Cloves - Ground",
        "price": 31.71
      }
    ]
  }, {
    "customerName": "Angelique",
    "status": "beforPayment",
    "items": [
      {
        "name": "Paper Towel Touchless",
        "price": 49.44
      }
    ]
  }, {
    "customerName": "Krysta",
    "status": "preparation",
    "items": [
      {
        "name": "Milk - Buttermilk",
        "price": 34.38
      },
      {
        "name": "Coffee - Dark Roast",
        "price": 44.26
      }
    ]
  }, {
    "customerName": "Ira",
    "status": "beforPayment",
    "items": [
      {
        "name": "Cup - 8oz Coffee Perforated",
        "price": 5.74
      },
      {
        "name": "Lid Coffeecup 12oz D9542b",
        "price": 7.83
      }
    ]
  }, {
    "customerName": "Josepha",
    "status": "ready",
    "items": [
      {
        "name": "Beef - Diced",
        "price": 37.19
      }
    ]
  }, {
    "customerName": "Ephrem",
    "status": "finish",
    "items": [
      {
        "name": "Silicone Parch. 16.3x24.3",
        "price": 44.33
      },
      {
        "name": "Bag Stand",
        "price": 34.15
      }
    ]
  }, {
    "customerName": "Hulda",
    "status": "finish",
    "items": [
      {
        "name": "Filter - Coffee",
        "price": 29.06
      }
    ]
  }, {
    "customerName": "Waylen",
    "status": "ready",
    "items": [
      {
        "name": "Cake Circle, Foil, Scallop",
        "price": 17.94
      }
    ]
  }, {
    "customerName": "Ruben",
    "status": "beforPayment",
    "items": [
      {
        "name": "Crab - Imitation Flakes",
        "price": 51.81
      },
      {
        "name": "Tomato - Peeled Italian Canned",
        "price": 16.72
      }
    ]
  }, {
    "customerName": "Gib",
    "status": "preparation",
    "items": [
      {
        "name": "Sour Cream",
        "price": 33.06
      },
      {
        "name": "Muffin Chocolate Individual Wrap",
        "price": 39.35
      },
      {
        "name": "Tea - Herbal Orange Spice",
        "price": 27.55
      }
    ]
  }, {
    "customerName": "Maud",
    "status": "ready",
    "items": [
      {
        "name": "Coffee - Cafe Moreno",
        "price": 54.25
      }
    ]
  }, {
    "customerName": "Stacia",
    "status": "ready",
    "items": [
      {
        "name": "Lettuce - Radicchio",
        "price": 36.19
      },
      {
        "name": "Soup Campbells - Italian Wedding",
        "price": 27.78
      },
      {
        "name": "Olives - Kalamata",
        "price": 7.83
      }
    ]
  }, {
    "customerName": "Jeramey",
    "status": "delivering",
    "items": [
      {
        "name": "Snails - Large Canned",
        "price": 28.73
      },
      {
        "name": "Beer - True North Strong Ale",
        "price": 53.18
      }
    ]
  }, {
    "customerName": "Tanitansy",
    "status": "delivering",
    "items": [
      {
        "name": "Pasta - Detalini, White, Fresh",
        "price": 31.76
      },
      {
        "name": "Peach - Fresh",
        "price": 37.33
      },
      {
        "name": "White Fish - Filets",
        "price": 18.64
      }
    ]
  }, {
    "customerName": "Vitia",
    "status": "finish",
    "items": [
      {
        "name": "Tia Maria",
        "price": 30.69
      },
      {
        "name": "Lotus Rootlets - Canned",
        "price": 10.59
      },
      {
        "name": "Pickerel - Fillets",
        "price": 12.25
      }
    ]
  }, {
    "customerName": "Kimberli",
    "status": "preparation",
    "items": [
      {
        "name": "Chicken - Whole Roasting",
        "price": 41.86
      },
      {
        "name": "Muffin Batt - Carrot Spice",
        "price": 7.17
      },
      {
        "name": "Vinegar - Cider",
        "price": 46.93
      }
    ]
  }, {
    "customerName": "Esra",
    "status": "preparation",
    "items": [
      {
        "name": "Whmis - Spray Bottle Trigger",
        "price": 52.54
      }
    ]
  }, {
    "customerName": "Rabbi",
    "status": "finish",
    "items": [
      {
        "name": "Cheese - Cambozola",
        "price": 28.01
      }
    ]
  }, {
    "customerName": "Orel",
    "status": "delivering",
    "items": [
      {
        "name": "Lemonade - Mandarin, 591 Ml",
        "price": 21.53
      }
    ]
  }, {
    "customerName": "Amabelle",
    "status": "ready",
    "items": [
      {
        "name": "Oil - Olive",
        "price": 32.61
      },
      {
        "name": "Bread Base - Gold Formel",
        "price": 58.88
      }
    ]
  }, {
    "customerName": "Joli",
    "status": "ready",
    "items": [
      {
        "name": "Bread - Multigrain Oval",
        "price": 7.59
      },
      {
        "name": "Pan Grease",
        "price": 20.5
      },
      {
        "name": "Marjoram - Dried, Rubbed",
        "price": 10.63
      }
    ]
  }, {
    "customerName": "Ware",
    "status": "preparation",
    "items": [
      {
        "name": "Sugar - Brown, Individual",
        "price": 21.58
      },
      {
        "name": "Wine - Periguita Fonseca",
        "price": 50.91
      }
    ]
  }, {
    "customerName": "Editha",
    "status": "beforPayment",
    "items": [
      {
        "name": "Pasta - Lasagna, Dry",
        "price": 50.61
      }
    ]
  }, {
    "customerName": "Verna",
    "status": "beforPayment",
    "items": [
      {
        "name": "Cheese - Cottage Cheese",
        "price": 18.64
      },
      {
        "name": "Crab - Meat Combo",
        "price": 18.07
      }
    ]
  }, {
    "customerName": "Inez",
    "status": "finish",
    "items": [
      {
        "name": "Pie Pecan",
        "price": 6.45
      },
      {
        "name": "Yogurt - French Vanilla",
        "price": 23.34
      }
    ]
  }, {
    "customerName": "Lu",
    "status": "ready",
    "items": [
      {
        "name": "Lamb - Shoulder",
        "price": 53.25
      },
      {
        "name": "Wine - Jackson Triggs Okonagan",
        "price": 5.65
      },
      {
        "name": "Wine - Chianti Classica Docg",
        "price": 55.84
      }
    ]
  }];