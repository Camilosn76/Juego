## Juegos ##
def YoNuncaNunca():
  n_1 = random.randint(0, len(Jugadores)-1)
  n_2 = random.randint(0, len(Preguntas)-1)
  
  html_content = f"""
    <div style="font-size: 30px; font-weight: none;">
        {Jugadores[n_1]}: Yo {Preguntas[n_2]}
    </div>
"""
  return display(HTML(html_content))

def Verdad_o_Reto():
  answer = ""
  n_1 = random.randint(0, len(Jugadores)-1)
  n_2 = random.randint(0, len(Preguntas)-1)
  n_3 = random.randint(0, len(Verdades)-1)
  n_4 = random.randint(0, len(Retos)-1)
  chooice = float(input (f"{Jugadores[n_1]}, ¿Verdad (0) o reto (1)?: "))
  
  
  if chooice == 0:
    print("\n")
    answer = str(Jugadores[n_1] + Verdades[n_3])
    answer = f"""
    <div style="font-size: 30px; font-weight: none;">
        {Jugadores[n_1]}, {Verdades[n_3]}
    </div>
"""
  if chooice == 1:
    print("\n")
    answer = str(Jugadores[n_1] + Retos[n_4])
    answer = f"""
    <div style="font-size: 30px; font-weight: none;">
        {Jugadores[n_1]}, debes {Retos[n_4]}
    </div>
"""

  return display(HTML(answer))
