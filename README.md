![](https://github.com/Johnng007/Anteater/blob/main/assets/logo.jpg?raw=true)

# 🤔 About Anteater

*Anteater is Reconnaissance tool for discovering interesting files and folders in a web application that most likely has been misconfigured to be accessible. Anteater is written in **Python3.x***
<p>Anteater discovers admin pages as well.</p>
<p>Anteater Aims at being very stealthy in its Admin page and Interesting file recon, this will allow it to bypass WAF triggers and successfully succeed in very sensitive web applications</p>

# 🥊 Installation

   * #### Git Clone 
      ```bash
      # Download and Usage
      ❯ git clone https://github.com/Johnng007/Anteater.git
      ❯ cd Anteater
      ❯ pip3 install -r requirements.txt
      ❯ chmod +x anteater.py
      ```

# 🔨 Usage

  * #### Main 

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
      
     # Insane Mode
     ❯ python3 anteater.py https://john.ng -p proxylist.txt -d 3 -t
     
     ```
     
## 🔥 Features
  
- [x] Multiplatforms `(Windows/Linux/MacOS)`
- [x] Detects Over 100+ Known CMS
- [x] Detects Over 1000 well known Admin Panels  
- [x] Random-Agents
- [x] Time delay in minutes between each request
- [x] HTTP/HTTPS Proxies
- [x] Anonymity via Tor

## 🔥 Screenshot

![](https://github.com/Johnng007/Anteater/blob/main/assets/Anteater-recon.png?raw=true)

## ✨ ChangeLog
```bash
v1.0.0 11/02/2023
Initial Release
```
