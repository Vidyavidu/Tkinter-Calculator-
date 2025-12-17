"""
Enhanced Scientific Calculator with Tkinter
Improvements: Error handling, OOP design, keyboard support, history
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.configure(bg="#293C4A", padx=10, pady=10)
        self.root.resizable(False, False)
        
        # Variables
        self.calc_operator = ""
        self.history = []
        
        # Create UI
        self.create_display()
        self.create_buttons()
        
        # Bind keyboard events
        self.root.bind('<Key>', self.key_press)
        self.root.bind('<Return>', lambda e: self.button_equal())
        self.root.bind('<BackSpace>', lambda e: self.button_delete())
        self.root.bind('<Escape>', lambda e: self.button_clear_all())
    
    def create_display(self):
        """Create the calculator display"""
        display_frame = tk.Frame(self.root, bg="#293C4A")
        display_frame.grid(row=0, column=0, columnspan=5, pady=(0, 15))
        
        self.text_input = tk.StringVar()
        self.text_display = tk.Entry(
            display_frame,
            font=('Consolas', 24, 'bold'),
            textvariable=self.text_input,
            bd=5,
            insertwidth=5,
            bg='#E8E8E8',
            fg='#000',
            justify='right',
            state='readonly'
        )
        self.text_display.pack(fill='x', padx=5)
    
    def create_buttons(self):
        """Create all calculator buttons"""
        button_params = {
            'bd': 3,
            'fg': '#E8E8E8',
            'bg': '#3C3636',
            'font': ('Arial', 16, 'bold'),
            'activebackground': '#4A4A4A'
        }
        button_params_main = {
            'bd': 3,
            'fg': '#000',
            'bg': '#D3D3D3',
            'font': ('Arial', 18, 'bold'),
            'activebackground': '#C0C0C0'
        }
        button_params_operator = {
            'bd': 3,
            'fg': '#FFF',
            'bg': '#FF9500',
            'font': ('Arial', 18, 'bold'),
            'activebackground': '#CC7700'
        }
        button_params_special = {
            'bd': 3,
            'fg': '#000',
            'bg': '#FF6B6B',
            'font': ('Arial', 16, 'bold'),
            'activebackground': '#CC5555'
        }
        
        # Button layout definition
        buttons = [
            # Row 1 - Scientific functions
            [('abs', lambda: self.button_click('abs('), button_params),
             ('mod', lambda: self.button_click('%'), button_params),
             ('div', lambda: self.button_click('//'), button_params),
             ('x!', self.fact_func, button_params),
             ('e', lambda: self.button_click(str(math.e)), button_params)],
            
            # Row 2 - Trig functions
            [('sin', self.trig_sin, button_params),
             ('cos', self.trig_cos, button_params),
             ('tan', self.trig_tan, button_params),
             ('cot', self.trig_cot, button_params),
             ('π', lambda: self.button_click(str(math.pi)), button_params)],
            
            # Row 3 - Powers
            [('x²', lambda: self.button_click('**2'), button_params),
             ('x³', lambda: self.button_click('**3'), button_params),
             ('xⁿ', lambda: self.button_click('**'), button_params),
             ('x⁻¹', lambda: self.button_click('**(-1)'), button_params),
             ('10ˣ', lambda: self.button_click('10**'), button_params)],
            
            # Row 4 - Roots and logs
            [('√', self.square_root, button_params),
             ('∛', self.third_root, button_params),
             ('ⁿ√', lambda: self.button_click('**(1/'), button_params),
             ('log', lambda: self.button_click('log10('), button_params),
             ('ln', lambda: self.button_click('log('), button_params)],
            
            # Row 5 - Parentheses and special
            [('(', lambda: self.button_click('('), button_params),
             (')', lambda: self.button_click(')'), button_params),
             ('±', self.sign_change, button_params),
             ('%', self.percent, button_params),
             ('eˣ', lambda: self.button_click('exp('), button_params)],
            
            # Row 6 - Numbers and clear
            [('7', lambda: self.button_click('7'), button_params_main),
             ('8', lambda: self.button_click('8'), button_params_main),
             ('9', lambda: self.button_click('9'), button_params_main),
             ('DEL', self.button_delete, button_params_special),
             ('AC', self.button_clear_all, button_params_special)],
            
            # Row 7 - Numbers and operators
            [('4', lambda: self.button_click('4'), button_params_main),
             ('5', lambda: self.button_click('5'), button_params_main),
             ('6', lambda: self.button_click('6'), button_params_main),
             ('×', lambda: self.button_click('*'), button_params_operator),
             ('÷', lambda: self.button_click('/'), button_params_operator)],
            
            # Row 8 - Numbers and operators
            [('1', lambda: self.button_click('1'), button_params_main),
             ('2', lambda: self.button_click('2'), button_params_main),
             ('3', lambda: self.button_click('3'), button_params_main),
             ('+', lambda: self.button_click('+'), button_params_operator),
             ('−', lambda: self.button_click('-'), button_params_operator)],
            
            # Row 9 - Zero, decimal, and equals
            [('0', lambda: self.button_click('0'), button_params_main),
             ('.', lambda: self.button_click('.'), button_params_main),
             ('EXP', lambda: self.button_click('*10**'), button_params_main),
             None,  # Placeholder for merged equal button
             None]
        ]
        
        # Create buttons
        for row_idx, row in enumerate(buttons, start=1):
            for col_idx, btn_info in enumerate(row):
                if btn_info is None:
                    continue
                
                text, command, params = btn_info
                btn = tk.Button(
                    self.root,
                    text=text,
                    command=command,
                    **params
                )
                
                # Equal button spans 2 columns
                if text == '=' or (row_idx == 9 and col_idx == 3):
                    continue
                    
                btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)
        
        # Create equal button (spans columns 3-4)
        equal_btn = tk.Button(
            self.root,
            text='=',
            command=self.button_equal,
            bd=3,
            fg='#FFF',
            bg='#4CAF50',
            font=('Arial', 18, 'bold'),
            activebackground='#45A049'
        )
        equal_btn.grid(row=9, column=3, columnspan=2, sticky="nsew", padx=2, pady=2)
        
        # Configure grid weights for responsive design
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1, minsize=80)
        for i in range(1, 10):
            self.root.grid_rowconfigure(i, weight=1, minsize=50)
    
    def button_click(self, char):
        """Add character to display"""
        self.calc_operator += str(char)
        self.text_input.set(self.calc_operator)
    
    def button_clear_all(self):
        """Clear all input"""
        self.calc_operator = ""
        self.text_input.set("")
    
    def button_delete(self):
        """Delete last character"""
        self.calc_operator = self.calc_operator[:-1]
        self.text_input.set(self.calc_operator)
    
    def safe_eval(self, expression):
        """Safely evaluate mathematical expression"""
        try:
            # Replace functions for eval
            safe_dict = {
                'abs': abs,
                'log10': math.log10,
                'log': math.log,
                'exp': math.exp,
                'sqrt': math.sqrt,
                '__builtins__': {}
            }
            result = eval(expression, safe_dict)
            return result
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")
    
    def fact_func(self):
        """Calculate factorial"""
        try:
            n = int(float(self.calc_operator))
            if n < 0:
                raise ValueError("Factorial not defined for negative numbers")
            if n > 170:
                raise ValueError("Number too large for factorial")
            result = math.factorial(n)
            self.calc_operator = str(result)
            self.text_input.set(self.calc_operator)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.button_clear_all()
    
    def trig_sin(self):
        """Calculate sine"""
        try:
            result = math.sin(math.radians(float(self.calc_operator)))
            self.calc_operator = str(result)
            self.text_input.set(self.calc_operator)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for sine")
            self.button_clear_all()
    
    def trig_cos(self):
        """Calculate cosine"""
        try:
            result = math.cos(math.radians(float(self.calc_operator)))
            self.calc_operator = str(result)
            self.text_input.set(self.calc_operator)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for cosine")
            self.button_clear_all()
    
    def trig_tan(self):
        """Calculate tangent"""
        try:
            result = math.tan(math.radians(float(self.calc_operator)))
            self.calc_operator = str(result)
            self.text_input.set(self.calc_operator)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for tangent")
            self.button_clear_all()
    
    def trig_cot(self):
        """Calculate cotangent"""
        try:
            angle = float(self.calc_operator)
            if angle % 180 == 0:
                raise ValueError("Cotangent undefined at multiples of 180°")
            result = 1 / math.tan(math.radians(angle))
            self.calc_operator = str(result)
            self.text_input.set(self.calc_operator)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.button_clear_all()
        except Exception:
            messagebox.showerror("Error", "Invalid input for cotangent")
            self.button_clear_all()
    
    def square_root(self):
        """Calculate square root"""
        try:
            num = float(self.calc_operator)
            if num < 0:
                raise ValueError("Cannot calculate square root of negative number")
            result = math.sqrt(num)
            self.calc_operator = str(result)
            self.text_input.set(self.calc_operator)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.button_clear_all()
    
    def third_root(self):
        """Calculate cube root"""
        try:
            num = float(self.calc_operator)
            result = num ** (1/3) if num >= 0 else -((-num) ** (1/3))
            self.calc_operator = str(result)
            self.text_input.set(self.calc_operator)
        except Exception:
            messagebox.showerror("Error", "Invalid input for cube root")
            self.button_clear_all()
    
    def sign_change(self):
        """Change sign of number"""
        try:
            if self.calc_operator:
                if self.calc_operator[0] == '-':
                    self.calc_operator = self.calc_operator[1:]
                else:
                    self.calc_operator = '-' + self.calc_operator
                self.text_input.set(self.calc_operator)
        except Exception:
            pass
    
    def percent(self):
        """Convert to percentage"""
        try:
            result = self.safe_eval(self.calc_operator) / 100
            self.calc_operator = str(result)
            self.text_input.set(self.calc_operator)
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression for percentage")
            self.button_clear_all()
    
    def button_equal(self):
        """Evaluate expression"""
        try:
            if self.calc_operator:
                result = self.safe_eval(self.calc_operator)
                self.history.append(f"{self.calc_operator} = {result}")
                self.calc_operator = str(result)
                self.text_input.set(self.calc_operator)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.button_clear_all()
        except Exception:
            messagebox.showerror("Error", "Invalid expression")
            self.button_clear_all()
    
    def key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        if key.isdigit() or key in '+-*/.()':
            self.button_click(key)


def main():
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
