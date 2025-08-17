#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
# Happy Birthday 
# github:https://github.com/xalidsabah
# Created May, aug 17 2025
# Copyright (c) 2025 XALID SABAH.
# Enhanced with ASCII art, advanced animations, and sound effects

import random
import time
import sys
import re
import os
import threading
import math
from typing import List, Tuple, Dict
from dataclasses import dataclass

# Python 2/3 compatibility
try:
    input = raw_input  # Python 2
except NameError:
    pass  # Python 3

# Enhanced color codes with XALID-style effects
class Colors:
    # Standard colors
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    RESET = '\033[0m'
    
    # Bright colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    
    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    
    # Special effects
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'

class SoundEngine:
    """Advanced sound engine with multiple sound effect capabilities"""
    
    def __init__(self):
        self.sound_enabled = True
        self.volume = 1.0  # 0.0 to 1.0
        self.platform = self._detect_platform()
    
    def _detect_platform(self):
        """Detect the operating system platform"""
        if os.name == 'nt':  # Windows
            return 'windows'
        elif os.name == 'posix':  # Unix/Linux/macOS
            return 'unix'
        else:
            return 'unknown'
    
    def beep(self, frequency=800, duration=200):
        """Generate a beep sound with specified frequency and duration"""
        if not self.sound_enabled:
            return
            
        try:
            if self.platform == 'windows':
                import winsound
                winsound.Beep(frequency, duration)
            elif self.platform == 'unix':
                # Use system beep command
                os.system(f'echo -e "\\a"')
                time.sleep(duration / 1000.0)
            else:
                # Fallback: just wait
                time.sleep(duration / 1000.0)
        except Exception:
            # Fallback if sound fails
            time.sleep(duration / 1000.0)
    
    def play_note(self, note, duration=500):
        """Play a musical note with specified duration"""
        note_frequencies = {
            'C': 261, 'C#': 277, 'D': 293, 'D#': 311, 'E': 329,
            'F': 349, 'F#': 369, 'G': 392, 'G#': 415, 'A': 440,
            'A#': 466, 'B': 493, 'C2': 523, 'D2': 587, 'E2': 659,
            'F2': 698, 'G2': 784, 'A2': 880, 'B2': 987
        }
        
        if note in note_frequencies:
            self.beep(note_frequencies[note], duration)
        else:
            # Default frequency if note not found
            self.beep(440, duration)
    
    def play_melody(self, melody, tempo=120):
        """Play a sequence of notes with specified tempo"""
        if not self.sound_enabled:
            return
            
        beat_duration = 60000 / tempo  # Convert BPM to milliseconds
        
        for note, beats in melody:
            if note == 'REST':
                time.sleep((beats * beat_duration) / 1000.0)
            else:
                self.play_note(note, int(beats * beat_duration))
                time.sleep(0.05)  # Small gap between notes
    
    def birthday_song(self):
        """Play the Happy Birthday song melody"""
        melody = [
            ('C', 1), ('C', 1), ('D', 2), ('C', 2), ('F', 2), ('E', 4),
            ('C', 1), ('C', 1), ('D', 2), ('C', 2), ('G', 2), ('F', 4),
            ('C', 1), ('C', 1), ('C2', 2), ('A', 2), ('F', 2), ('E', 2), ('D', 4),
            ('A#', 1), ('A#', 1), ('A', 2), ('F', 2), ('G', 2), ('F', 4)
        ]
        self.play_melody(melody, tempo=100)
    
    def celebration_sounds(self):
        """Play celebration sound effects"""
        # Fanfare
        fanfare = [
            ('C', 0.5), ('E', 0.5), ('G', 0.5), ('C2', 1),
            ('G', 0.5), ('E', 0.5), ('C', 1)
        ]
        self.play_melody(fanfare, tempo=140)
    
    def explosion_sound(self):
        """Play explosion sound effect"""
        # Descending tone for explosion
        for freq in [800, 600, 400, 200]:
            self.beep(freq, 100)
    
    def sparkle_sound(self):
        """Play sparkle sound effect"""
        # Ascending sparkle tones
        for freq in [400, 600, 800, 1000]:
            self.beep(freq, 50)
    
    def cake_sound(self):
        """Play cake preparation sound"""
        # Gentle ascending tones
        for freq in [300, 400, 500]:
            self.beep(freq, 200)
    
    def victory_fanfare(self):
        """Play victory fanfare sound"""
        victory = [
            ('C', 0.5), ('E', 0.5), ('G', 0.5), ('C2', 1),
            ('C2', 0.5), ('G', 0.5), ('C2', 2)
        ]
        self.play_melody(victory, tempo=120)
    
    def disable_sound(self):
        """Disable sound effects"""
        self.sound_enabled = False
    
    def enable_sound(self):
        """Enable sound effects"""
        self.sound_enabled = True
    
    def set_volume(self, volume):
        """Set sound volume (0.0 to 1.0)"""
        self.volume = max(0.0, min(1.0, volume))

@dataclass
class Particle:
    """Particle system for advanced effects"""
    x: float
    y: float
    vx: float
    vy: float
    char: str
    color: str
    life: int
    max_life: int

class AnimationEngine:
    """Advanced animation engine with particle systems and sound integration"""
    
    def __init__(self, sound_engine: SoundEngine):
        self.particles: List[Particle] = []
        self.screen_width = 80
        self.screen_height = 25
        self.sound_engine = sound_engine
    
    def add_particle(self, x: float, y: float, char: str, color: str, life: int = 30):
        """Add a new particle to the system"""
        vx = random.uniform(-2, 2)
        vy = random.uniform(-3, -1)
        self.particles.append(Particle(x, y, vx, vy, char, color, life, life))
    
    def update_particles(self):
        """Update all particles in the system"""
        for particle in self.particles[:]:
            particle.x += particle.vx
            particle.y += particle.vy
            particle.vy += 0.1  # Gravity
            particle.life -= 1
            
            if particle.life <= 0 or particle.y > self.screen_height:
                self.particles.remove(particle)
    
    def render_particles(self):
        """Render all particles to screen"""
        screen = [[' ' for _ in range(self.screen_width)] for _ in range(self.screen_height)]
        
        for particle in self.particles:
            x, y = int(particle.x), int(particle.y)
            if 0 <= x < self.screen_width and 0 <= y < self.screen_height:
                screen[y][x] = particle.char
        
        # Clear screen and render
        clear_screen()
        for row in screen:
            print(''.join(row))
    
    def create_explosion(self, x: float, y: float, intensity: int = 20):
        """Create a particle explosion with sound"""
        chars = ['*', '+', 'o', 'x', '~', '^', 'v', '<', '>']
        colors = [Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN]
        
        # Play explosion sound
        self.sound_engine.explosion_sound()
        
        for _ in range(intensity):
            char = random.choice(chars)
            color = random.choice(colors)
            self.add_particle(x, y, char, color, random.randint(20, 40))

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def rainbow_text(text: str, delay: float = 0.05, sound_engine: SoundEngine = None) -> None:
    """Display text with rainbow color cycling effect and optional sound"""
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(f"{color}{char}", end='', flush=True)
        
        # Play sparkle sound for certain characters
        if sound_engine and char in '!*@#$%^&*':
            sound_engine.sparkle_sound()
        
        time.sleep(delay)
    print(Colors.RESET)

def typewriter_effect(text: str, delay: float = 0.03, color: str = Colors.WHITE, sound_engine: SoundEngine = None) -> None:
    """Display text with typewriter effect and optional sound"""
    for char in text:
        print(f"{color}{char}", end='', flush=True)
        
        # Play typewriter sound
        if sound_engine and char != ' ':
            sound_engine.beep(1000, 10)
        
        time.sleep(delay)
    print(Colors.RESET)

def matrix_rain_effect(duration: int = 5, sound_engine: SoundEngine = None):
    """Matrix-style rain effect with XALID characters and sound"""
    chars = ['█', '▓', '▒', '░', '▄', '▌', '▐', '▀', '▖', '▗', '▘', '▙', '▚', '▛', '▜', '▝', '▞', '▟']
    colors = [Colors.GREEN, Colors.BRIGHT_GREEN, Colors.CYAN]
    
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(10):
            char = random.choice(chars)
            color = random.choice(colors)
            x = random.randint(0, 79)
            y = random.randint(0, 24)
            print(f"\033[{y};{x}H{color}{char}", end='', flush=True)
            
            # Play matrix sound occasionally
            if sound_engine and random.random() < 0.1:
                sound_engine.beep(random.randint(200, 800), 50)
        
        time.sleep(0.1)
        print("\033[2J", end='', flush=True)

def xalid_banner_animation(sound_engine: SoundEngine = None):
    """Display XALID-style animated banners with sound"""
    banners = [
        # XALID-style banner 1
        f"""{Colors.BRIGHT_RED}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  ██╗ █████╗ ██╗     ██╗██████╗     ██████╗ ██████╗ ██╗   ██╗███████╗    ║
║  ██║██╔══██╗██║     ██║██╔══██╗    ██╔═══██╗██╔═══██╗██║   ██║██╔════╝    ║
║  ██║███████║██║     ██║██║  ██║    ██║   ██║██║   ██║██║   ██║█████╗      ║
║  ██║██╔══██║██║     ██║██║  ██║    ██║   ██║██║   ██║╚██╗ ██╔╝██╔══╝      ║
║  ██║██║  ██║███████╗██║██████╔╝    ╚██████╔╝╚██████╔╝ ╚████╔╝ ███████╗    ║
║  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═════╝      ╚═════╝  ╚═════╝   ╚═══╝  ╚══════╝    ║
║                                                                              ║
║                    🎉 ULTIMATE BIRTHDAY CELEBRATION 🎉                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
        """,
        
        # XALID-style banner 2
        f"""{Colors.BRIGHT_BLUE}
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  │
│  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  │
│  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  │
│  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  █  │
│  █  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  █  │
│  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  │
│                                                                              │
│                    🌟 XALID STYLE CELEBRATION 🌟                            │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}
        """,
        
        # XALID-style banner 3
        f"""{Colors.BRIGHT_MAGENTA}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  ███████╗██╗  ██╗ █████╗ ██╗     ██████╗     ███████╗████████╗██╗   ██╗  ║
║  ██╔════╝██║  ██║██╔══██╗██║     ██╔══██╗    ██╔════╝╚══██╔══╝██║   ██║  ║
║  ███████╗███████║███████║██║     ██║  ██║    █████╗     ██║   ██║   ██║  ║
║  ╚════██║██╔══██║██╔══██║██║     ██║  ██║    ██╔══╝     ██║   ██║   ██║  ║
║  ███████║██║  ██║██║  ██║███████╗██████╔╝    ███████╗   ██║   ╚██████╔╝  ║
║  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝     ╚══════╝   ╚═╝    ╚═════╝   ║
║                                                                              ║
║                    🎊 ADVANCED PARTICLE SYSTEM 🎊                          ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
        """
    ]
    
    for i, banner in enumerate(banners):
        clear_screen()
        print(banner)
        
        # Play banner transition sound
        if sound_engine:
            sound_engine.beep(600 + i * 100, 200)
        
        time.sleep(2)

def advanced_cake_animation(sound_engine: SoundEngine = None):
    """Enhanced cake animation with XALID characters and sound"""
    cake_frames = [
        f"""{Colors.YELLOW}
        🎂
        🕯️🕯️🕯️
        ████████
        ████████
        ████████
        ████████{Colors.RESET}""",
        
        f"""{Colors.BRIGHT_YELLOW}
        🎂
        🕯️🕯️🕯️
        ▓▓▓▓▓▓▓▓
        ████████
        ████████
        ████████{Colors.RESET}""",
        
        f"""{Colors.BRIGHT_CYAN}
        🎂
        🕯️🕯️🕯️
        ▒▒▒▒▒▒▒▒
        ▓▓▓▓▓▓▓▓
        ████████
        ████████{Colors.RESET}"""
    ]
    
    for i, frame in enumerate(cake_frames):
        clear_screen()
        print(frame)
        
        # Play cake building sound
        if sound_engine:
            sound_engine.cake_sound()
        
        time.sleep(0.8)

def particle_fireworks(sound_engine: SoundEngine = None):
    """Advanced fireworks using particle system with sound"""
    engine = AnimationEngine(sound_engine)
    
    for i in range(5):
        x = random.randint(20, 60)
        y = random.randint(5, 15)
        engine.create_explosion(x, y, 30)
        
        for _ in range(10):
            engine.update_particles()
            engine.render_particles()
            time.sleep(0.1)

def spinning_animation(text: str, rotations: int = 3, sound_engine: SoundEngine = None):
    """Enhanced spinning text animation with sound"""
    spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    
    for _ in range(rotations * len(spinner_chars)):
        spinner = spinner_chars[_ % len(spinner_chars)]
        print(f"\r{Colors.CYAN}{spinner} {text}", end='', flush=True)
        
        # Play spinner sound occasionally
        if sound_engine and _ % 5 == 0:
            sound_engine.beep(800, 50)
        
        time.sleep(0.1)
    print()

def validate_name(name: str) -> bool:
    """Validate and sanitize the input name"""
    if not name or not name.strip():
        return False
    if not re.match(r'^[a-zA-Z0-9\s\'-]+$', name.strip()):
        return False
    return True

def safe_input(prompt: str, max_length: int = 50) -> str:
    """Safely get user input with validation"""
    try:
        user_input = input(prompt).strip()
        if len(user_input) > max_length:
            print(f"{Colors.RED}[-] Input too long. Maximum {max_length} characters allowed.{Colors.RESET}")
            return None
        return user_input
    except (EOFError, KeyboardInterrupt):
        print(f"\n{Colors.RED}[-] Input interrupted. Exiting...{Colors.RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}[-] Error reading input: {e}{Colors.RESET}")
        return None

def ultimate_celebration(name: str, sound_engine: SoundEngine):
    """Ultimate birthday celebration with all effects and sound"""
    clear_screen()
    
    # Matrix rain effect with sound
    print(f"{Colors.BRIGHT_GREEN}🎬 Initializing advanced celebration systems...{Colors.RESET}")
    time.sleep(1)
    matrix_rain_effect(3, sound_engine)
    
    # Cake animation with sound
    print(f"{Colors.YELLOW}🎂 Preparing your XALID-style birthday cake... 🎂{Colors.RESET}")
    time.sleep(1)
    advanced_cake_animation(sound_engine)
    
    # Particle fireworks with sound
    print(f"{Colors.MAGENTA}🎆 Launching advanced particle fireworks! 🎆{Colors.RESET}")
    time.sleep(1)
    particle_fireworks(sound_engine)
    
    clear_screen()
    
    # Main celebration
    print(f"{Colors.BRIGHT_GREEN}{'═'*60}{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}🎉 HAPPY BIRTHDAY {name.upper()}! 🎉{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}{'═'*60}{Colors.RESET}\n")
    
    # Play birthday song
    print(f"{Colors.BRIGHT_CYAN}🎵 Playing Happy Birthday song... 🎵{Colors.RESET}")
    sound_engine.birthday_song()
    
    # Enhanced birthday song display
    song_lines = [
        "🎵 Happy Birthday to You... 🎵",
        "🎵 Happy Birthday to You... 🎵",
        f"🎵 Happy Birthday Dear {name}... 🎵",
        "🎵 Happy Birthday to You! 🎵"
    ]
    
    for line in song_lines:
        rainbow_text(line, 0.08, sound_engine)
        time.sleep(1)
    
    print()
    
    # Advanced Hip Hip Hooray with sound
    for i in range(3):
        print(f"{Colors.BRIGHT_BLUE}🎊 Hip Hip Hooray! 🎊{Colors.RESET}")
        sound_engine.beep(600, 200)
        time.sleep(0.3)
        print(f"{Colors.BRIGHT_GREEN}🎉 Hip Hip Hooray! 🎉{Colors.RESET}")
        sound_engine.beep(700, 200)
        time.sleep(0.3)
        print(f"{Colors.BRIGHT_MAGENTA}🎊 Hip Hip Hooray! 🎊{Colors.RESET}")
        sound_engine.beep(800, 200)
        time.sleep(0.8)
        print()
    
    # Final celebration with XALID style and sound
    print(f"{Colors.BRIGHT_YELLOW}{'═'*60}{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}🎂 Happy Birthday {name}! 🎂{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}🌟 Have an amazing day filled with joy! 🌟{Colors.RESET}")
    print(f"{Colors.BRIGHT_MAGENTA}🎁 May all your wishes come true! 🎁{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}{'═'*60}{Colors.RESET}")
    
    # Victory fanfare
    sound_engine.victory_fanfare()
    
    # Final particle burst with sound
    time.sleep(2)
    engine = AnimationEngine(sound_engine)
    engine.create_explosion(40, 12, 50)
    for _ in range(15):
        engine.update_particles()
        engine.render_particles()
        time.sleep(0.1)

def main():
    """Main function with ultimate animations and sound"""
    try:
        # Initialize sound engine
        sound_engine = SoundEngine()
        
        # Check if user wants sound
        print(f"{Colors.BRIGHT_CYAN}🔊 Sound Effects Enabled! 🔊{Colors.RESET}")
        print(f"{Colors.BRIGHT_GREEN}Press Enter to continue with sound, or type 'mute' to disable...{Colors.RESET}")
        
        sound_choice = input().strip().lower()
        if sound_choice == 'mute':
            sound_engine.disable_sound()
            print(f"{Colors.YELLOW}🔇 Sound effects disabled{Colors.RESET}")
        else:
            print(f"{Colors.BRIGHT_GREEN}🔊 Sound effects enabled!{Colors.RESET}")
        
        time.sleep(1)
        
        # XALID banner animation with sound
        xalid_banner_animation(sound_engine)
        
        # Welcome message
        clear_screen()
        print(f"{Colors.BRIGHT_CYAN}{'═'*60}{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}🎉 Welcome to the ULTIMATE XALID Birthday Celebration! 🎉{Colors.RESET}")
        print(f"{Colors.BRIGHT_GREEN}🌟 Experience the most advanced birthday program ever! 🌟{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}{'═'*60}{Colors.RESET}\n")
        
        time.sleep(2)
        
        # Loading animation with sound
        spinning_animation("Initializing XALID celebration systems...", 3, sound_engine)
        
        # Get user's name
        first_name = None
        while not first_name:
            first_name = safe_input(f"{Colors.BRIGHT_GREEN}[+] Enter your first name: {Colors.RESET}")
            if first_name and not validate_name(first_name):
                print(f"{Colors.RED}[-] Invalid name. Please use only letters, numbers, spaces, hyphens, and apostrophes.{Colors.RESET}")
                first_name = None
        
        if not first_name:
            print(f"{Colors.RED}[-] Could not get valid input. Exiting...{Colors.RESET}")
            return
        
        # Start ultimate celebration with sound
        print(f"\n{Colors.BRIGHT_YELLOW}🎊 Let's celebrate {first_name}'s birthday with XALID style and sound! 🎊{Colors.RESET}")
        time.sleep(2)
        
        ultimate_celebration(first_name, sound_engine)
        
        # Final message with celebration sound
        print(f"\n{Colors.BRIGHT_GREEN}🎉 Thank you for experiencing the ULTIMATE XALID Birthday Celebration! 🎉{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}🌟 This is the most advanced birthday program in existence! 🌟{Colors.RESET}")
        
        # Final celebration sound
        sound_engine.celebration_sounds()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[-] Program interrupted by user. Exiting...{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}[-] An unexpected error occurred: {e}{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
