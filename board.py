import json

import pyttsx3

msg =[]
data =[]
file_name ="dat.json"
def load_data():
    try:
        with open(file_name ,"r")as f:
            json.load(f)
    except FileNotFoundError:
        print("file not found error")
def save_data():
    with open(file_name,"w") as f:
        json.dump(data,f,indent=4)




def data_store():
    prime ={
        "What is Forming":"bro I want full information about the forming and what's ingredians are used and I want In format he",
        "Common Ingredients":"The ingredients used in forming depend entirely on whether you are in a factory making metal parts or a food plant making snacks.In Industrial Manufacturing (Metals/Plastics):Metals: Steel, aluminium, copper, brass, and titanium are the most common. These are chosen for their ductility (ability to be stretched) and yield strength.Polymers: Synthetic plastics like PVC, polyethylene, and polypropylene are used in plastic extrusion and moulding.Auxiliary Materials: Lubricants (to reduce friction between the material and the die) and binders are often added during the process.In Food Manufacturing:Base Ingredients: High-viscosity materials like wheat flour (for dough), starches, and proteins (soy or animal-based).Additives: Emulsifiers (like soy lecithin) and stabilizers are used to ensure the food holds its shape after forming.Binding Agents: Fats, oils, and water are critical to making the mixture pliable enough to be formed through a machine.",
        "Key Types":"There are several ways to form a material into a final product:Extrusion: Forcing a material through a shaped hole (die). Think of it like squeezing toothpaste out of a tube. This is used for making metal pipes, plastic window frames, and even pasta or snacks.Rolling: Passing a material between rotating rollers to reduce its thickness. This is how metal sheets and flatbreads are made.Forging: Using hammers or presses to squeeze metal into a high-strength shape (e.g., gears, bolts, or tools).Deep Drawing: Pressing a flat sheet of material into a hollow cup or box shape. This is how soda cans and kitchen sinks are formed.4. Why Use Forming?Material Efficiency: Since no material is cut away, there is almost zero waste.Improved Strength: The process of squeezing material often aligns its internal grains, making the final part stronger than if it were cast or machined.Speed: Modern forming machines can produce thousands of identical parts (like nails or biscuits) in very short timeframes.",
        "Definition":"Forming is a primary manufacturing technique that uses plastic deformation to reshape a solid body. It involves applying stresses like compression, tension, or shear to force a material into a specific geometry while maintaining its total mass.",
    }  
    data.append(prime)  
save_data()
data_store()
def chat():
    ask =input("Enter your question:")

    if "definition" in ask:
             
        print("defination:",data[0]["Definition"])
        return data[0]["Defination"]
    elif "ingredients" in ask:
        print("common ingredients in using forming:\n",data[0]["Common Ingredients"])
        return data[0]["Common Ingredients"]
    
    elif "forming" in ask:
        print("key types of forming:\n",data[0]["Key Types"])
        return data[0]["Key Types"]
    elif "what is forming" in ask:
        print("whats forming:\n",data[0]["What is Forming"])
        return data[0]["What is Forming"]
    elif "hi" and "how are you" in ask:
        print(" i am well what about you bro")
        return "well how are you"
    else:
        print("sorry i didn't found data")
        return "sorry didn't found"
save_data()
re =chat()
while True:
   def speak():
     engine =pyttsx3.init()
     engine.say(re)
     engine.runAndWait()
     return "answer ready....."
   speak()

   while True:

    print("type enter__ if you want to loging")
    choice =input("Enter your choice:")
    

    if choice =="enter":
        chat()
        
    elif choice =="exit":
        exit()
        break
   
    else:
        print("sorry")
re =chat()
def speak():
    engine =pyttsx3.init()
    engine.say(re)
    engine.runAndWait()
    return "answer ready....."
speak()


