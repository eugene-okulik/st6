import os
import glob
import argparse


def find_text_with_context_by_line(text, word, before_context_size=100, after_context_size=100):
    results = {}
    lines = text.split('\n')
    word_len = len(word)

    for i, line in enumerate(lines, start=1):
        for j in range(len(line)):
            if line[j:j + word_len] == word:
                start_index = max(0, j - before_context_size)
                context_before = line[start_index:j]

                context_after = ''
                remaining_length = after_context_size
                line_index = i - 1
                offset = j + word_len

                while remaining_length > 0 and line_index < len(lines):
                    start_point = offset if line_index == i - 1 else 0
                    end_point = min(len(lines[line_index]), start_point + remaining_length)

                    context_after += lines[line_index][start_point:end_point]

                    remaining_length -= end_point - start_point
                    line_index += 1
                    offset = 0

                context = context_before + word + context_after
                results[i] = context.strip()
                break

    return results


def read_logs_from_directory(directory, filename_pattern):
    log_texts = []
    for filepath in glob.glob(os.path.join(directory, filename_pattern)):
        with open(filepath, 'r') as file:
            log_texts.append((filepath, file.read()))
    return log_texts


def main():
    parser = argparse.ArgumentParser(description='Поиск текста в файлах логов')
    parser.add_argument('--directory', type=str, help='Путь к директории с лог-файлами', required=True)
    parser.add_argument('--word', type=str, help='Искомое слово', required=True)

    args = parser.parse_args()

    filename_pattern = '*.log'

    log_files = read_logs_from_directory(args.directory, filename_pattern)

    for filepath, log_text in log_files:
        results = find_text_with_context_by_line(log_text, args.word)
        if results:
            print(f"Результаты поиска в файле: {os.path.basename(filepath)}")
            for line_number, context in results.items():
                print(f"Строка {line_number}: {context}")


if __name__ == "__main__":
    main()
