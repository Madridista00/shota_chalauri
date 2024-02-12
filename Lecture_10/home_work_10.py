# დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის გამოყენებით "https://fakestoreapi.com/products" მისამართზე, შეამოწმებს 
# სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:

# ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები

# ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ 

# გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით

# დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით


import requests

def get_products():
  try:
    api_url = "https://fakestoreapi.com/products"
    response = requests.get(api_url)

    # print(response)
    print(response.status_code,"\n")
    # print(response.text)

    if response.status_code != 200:
      print(f"ERROR: can't get data. Status {response.status_code}")
      return False
    
    return response.json()
  except requests.exceptions.HTTPError as http_err:
    print(f"ERROR: {http_err}")
  except requests.exceptions.ConnectionError as con_err:
    print(f"Connectio error: {con_err}")
  except Exception as err:
    print("Something wrong! {err}")


def parese_data():
  products = get_products()

  products_price = [] 
  products_category = set()
  products_title = []
  product_rate = []

  print(products[0].keys(), "\n")

  for product in  products:
    products_price.append(product['price'])
    products_category.add(product['category'])
    products_title.append({'id': product['id'], 'title': product['title']})
    product_rate.append(product['rating'])
    


# ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები
  print(f"list of product_price is: {products_price}", "\n")
  print(f"min product price is: {min(products_price)}", "\n")
  print(f"max product price is: {max(products_price)}", "\n")
  print(f"sum of product price is: {sum(products_price) / len(products_price)}", "\n\n")


# ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ
  print(f"Product category is: {sorted(products_category)}", "\n\n")

# გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით
  sorted_product_title = sorted(products_title, key=lambda d: d['title'])
  print(f"Sorted product with title is: {sorted_product_title}", "\n\n")

# დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით
  sorted_product_rate = sorted(product_rate, key=lambda d: d['rate'])
  print(f"Sorted product with rate is: {sorted_product_rate}")

  




# ===================
parese_data()