# 🎨 Python Greeting Script 🎉

print("✨ Welcome to the Magical Greeting Generator! ✨\n")

# Ask user for details
name = input("👋 What's your name? ")
age = input("🎂 How old are you? ")
color = input("🌈 What's your favorite color? ")

# Create a fun, personalized message
print("\n🪄 Generating your custom message...\n")

# Add a little drama with dots
import time
for dot in "...":
    print(dot, end='', flush=True)
    time.sleep(0.5)

# Final personalized message
print(f"""

🌟 Hello {name}! 🌟
At {age} years young, you're already shining bright!
Your love for the color {color} shows you have a vibrant soul.

Keep being awesome and spreading colorful vibes! 🎉

""")
# End of the script