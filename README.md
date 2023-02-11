![](https://github.com/Johnng007/Anteater/blob/main/assets/logo.jpg?raw=true)

# 🤔 ABOUT ANTEATER

*Anteater is Reconnaissance tool for discovering interesting files and folders in a web application that most likely has been misconfigured to be accessible. Anteater is written in **Python3.x***
<p>Anteater discovers admin pages as well.</p>

# 🥊 INSTALLATION

   * #### Git Clone 
      ```bash
      # Download and Usage
      ❯ git clone https://github.com/Johnng007/Anteater.git
      ❯ cd Anteater
      ❯ pip3 install -r requirements.txt
      ❯ chmod +x anteater.py
      ```

# 🔨 USAGE

      ```bash
      # Help
      ❯ python3 anteater -h
      
      # Default
      ❯ python3 anteater.py https://john.ng
      
      # Time Delay in Minutes
      ❯ python3 anteater.py https://john.ng -d 3
      
      # Parse all connections through tor
      ❯ python3 anteater.py https://john.ng -t
      
      # Parse all connections through a Proxy List
      ❯ python3 anteater.py https://john.ng -p proxylist.txt
      
      # Of course you can be very insane
      ❯ python3 anteater.py https://john.ng -p proxylist.txt -d 3 -t
      ```
