import interaction.comm as comm

if __name__ == "__main__":
   try:
      comm.init()
   except Exception as e:
      print(f"An error occurred: {e}")