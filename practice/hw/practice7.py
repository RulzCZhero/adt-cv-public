def clean_subjects(data:list[str]) ->list[str]:
 better_data = set(data)
 cleaned_data = list(better_data)
 cleaned_data.sort()
 return cleaned_data
def main():
 raw_data = ["KIV/ZPR", "KIV/UPG", "KIV/ZPR", "MA1", "KIV/UPG", "KIV/ZPR", "MA1", "KIV/TI"]
 cleaned_data = clean_subjects(raw_data)
 print(F"Cleaned up data: {cleaned_data}")


if __name__=='__main__':
 main()