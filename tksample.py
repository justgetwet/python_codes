import tkinter as tk
from tkinter import ttk
import pandas as pd
import seaborn as sns
import unicodedata

def main():
  root = tk.Tk()
  root.title("tk sample")
  table_title = "this is title."
  root.geometry("500x250")

  f_toolbar = tk.Frame(root, bg="whitesmoke", height=50, width=500, pady=10, padx=10)
  f_toolbar.pack(fill=tk.X)
  
  l_title = tk.Label(f_toolbar, text=table_title, bg="whitesmoke", anchor="w")
  l_title.pack(side=tk.LEFT, expand=True, anchor=tk.W)

  b_quit = ttk.Button(f_toolbar, text='Quit', command=lambda: root.quit())
  b_quit.pack(side=tk.LEFT, expand=True, anchor=tk.E)

  f_main = tk.Frame(root, height=200, width=500, pady=10, padx=10)
  # set_table(f_main)
  f_main.pack(fill=tk.BOTH)
  
  root.mainloop()

def set_table(frame):
  
  iris = sns.load_dataset('iris')
  df = iris.head(6)
  headingcolor = "lightgrey"
  alternatecolor = "whitesmoke"

  tree = ttk.Treeview(frame, height=len(df)+1)

  def fixed_map(option):
    # Fix for setting text colour for Tkinter 8.6.9
    # From: https://core.tcl.tk/tk/info/509cafafae
    #
    # Returns the style map for 'option' with any styles starting with
    # ('!disabled', '!selected', ...) filtered out.
    #
    # style.map() returns an empty list for missing options, so this
    # should be future-safe.
    return [elm for elm in style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]	
  
  style = ttk.Style()
  style.theme_use("default")
  style.configure("Treeview.Heading", background=headingcolor)
  style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))
  # s.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))
  
  tree["show"] = "headings"
  cols = tuple(range(1, len(df.columns)+1))
  tree['columns'] = cols
  sizes = column_sizes(df)
  for i, col, size in zip(cols, df.columns, sizes):
    tree.heading(i, text=f"{col}")
    tree.column(i, width=size+8) # 
  
  lst = [tuple(t)[1:] for t in df.itertuples()]
  for i, tpl in enumerate(lst):
    tree.insert("", "end", tags=i, values=tpl)
    if i & 1:
      tree.tag_configure(i, background=alternatecolor)
  
  tree.pack(pady=10, padx=10)

def column_sizes(df: pd.DataFrame) -> list:

  def ea_width_count(text):
    count = 0
    for c in text:
      if unicodedata.east_asian_width(c) in 'FWA':
        count += 2
      else:
        count += 1
    return count * 8
  
  lst_columns = [[col] + list(df[col]) for col in df.columns]
  col_sizes = []
  for lst in lst_columns:
    col_sizes.append(max([ea_width_count(str(e)) for e in lst]))

  return col_sizes

if __name__ == '__main__':

  main()