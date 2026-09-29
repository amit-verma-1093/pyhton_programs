import wikipedia

def choose_language():
    lang = input("Choose language (en/hi): ").strip().lower()
    if lang not in ["en", "hi"]:
        print("Invalid choice, defaulting to English.\n")
        lang = "en"
    wikipedia.set_lang(lang)

def get_topic():
    topic = input("\nEnter topic (or 'exit'): ").strip()
    if not topic:
        print("Please enter a valid topic.")
        return None
    return topic

def fetch_summary(topic):
    try:
        return wikipedia.summary(topic, sentences=3)
    
    except wikipedia.exceptions.DisambiguationError as e:
        print("\nMultiple results found:")
        for i, option in enumerate(e.options[:5], 1):
            print(f"{i}. {option}")
        
        try:
            choice = int(input("Choose an option (1-5): "))
            selected = e.options[choice - 1]
            print("\nFetching result...\n")
            return wikipedia.summary(selected, sentences=3)
        except:
            print("Invalid choice.")
            return None

    except wikipedia.exceptions.PageError:
        print("Page not found. Try another topic.")
        return None

    except Exception as e:
        print("Something went wrong:", e)
        return None

def fetch_full_article(topic):
    try:
        page = wikipedia.page(topic)
        return page.content
    except Exception as e:
        print("Error fetching full article:", e)
        return None

def save_to_file(content):
    try:
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved to output.txt")
    except Exception as e:
        print("Error saving file:", e)

def main():
    print("=== Mini Wikipedia App ===")
    choose_language()

    while True:
        topic = get_topic()

        if topic is None:
            continue

        if topic.lower() == "exit":
            print("Goodbye!")
            break

        print("\nSearching Wikipedia...\n")

        mode = input("Do you want full article? (y/n): ").lower()

        if mode == "y":
            content = fetch_full_article(topic)
        else:
            content = fetch_summary(topic)

        if content:
            print("\nResult:\n")
            print(content[:2000])  # limit output

            save = input("\nSave to file? (y/n): ").lower()
            if save == "y":
                save_to_file(content)

if __name__ == "__main__":
    main()