def start_program(data: dict):
    assert isinstance(data, dict), "Invalid JSON"
    assert data, "No data found..."

    print("Loaded successfully!")


if __name__ == "__main__":
    json = {"User": 123}
    start_program(data=json)
    print(__debug__)
    
    
    






# https://www.youtube.com/watch?v=96mDQrlceEk
