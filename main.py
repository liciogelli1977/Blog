# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


quote1 = "Your support emotional Russian believes in you"
quote2 = "You cannot falling apart, if you simply refuse"
contenuto_html = f"""
<!DOCTYPE html>
<html>


<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=2.0">
	<meta http-equiv="X-UA-Compatible" content="IE-edge">
	<title> Capstone  </title>
	<link rel="stylesheet" href="style.css"/>
</head>


<body>
    	<h1> - {quote1} -  </h1>

    <a target="_blank" href="agentin.gif">
    <img src="agentin.gif" alt="KGBagentin" width="509" height="666">
  </a>

		<h3>:{quote2}</h3>
</body>
</html>
"""

with open("pagina.html", "w") as f:
    f.write(contenuto_html)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
