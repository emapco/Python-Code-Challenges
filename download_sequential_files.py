import os
import re
import urllib
import requests


# downloads and saves a sequence of files. Determines all numbers in link
# to be incremented and pings them.
# EX: 699340 and 001 in http://699340.youcanlearnit.net/image001.jpg
def download_files(link, output_dir_path):
    if not os.path.exists(output_dir_path):
        os.mkdir(output_dir_path)

    try:
        response = requests.get(link)
        if response.status_code != 200:  # link not valid so stop process
            return
        with open(output_dir_path + '\\' + os.path.basename(link), 'wb') as file:
            file.write(response.content)
            print('Downloading image at ', link)
    except (requests.HTTPError, requests.ConnectionError):
        return

    # match every sequence of digits in link
    possible_sequences = [x for x in re.findall(r"\d*", link) if x]
    for num_match in possible_sequences:  # increment each match and send it a request
        error_count = 0
        try:
            num_match_index = link.find(num_match)
            next_sequence_num = int(num_match)
            while error_count < 3:
                next_sequence_num += 1
                next_sequence_str = str(next_sequence_num)
                last_digit_sequence_index = num_match_index + len(num_match)
                if num_match[0] == '0':  # if zero padded then pad
                    next_sequence_str = '0' * (len(num_match) - len(next_sequence_str)) + next_sequence_str
                next_link = link[:num_match_index] + str(next_sequence_str) + link[last_digit_sequence_index:]

                response = requests.get(next_link)
                if response.status_code != 200:  # if not valid link, continue to next link
                    error_count += 1
                    continue
                with open(output_dir_path + '\\' + os.path.basename(next_link), 'wb') as file:
                    file.write(response.content)
                    print('Downloading image at ', next_link)
        except (requests.HTTPError, requests.ConnectionError):
            pass

def solution(first_url, output_dir):
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    url_head, url_tail = os.path.split(first_url)
    first_index = re.findall(r'[0-9]+', url_tail)[-1]
    index_count, error_count = 0, 0

    while error_count < 5:
        next_index = str(int(first_index) + index_count)
        if first_index[0] == '0': # zero padded
            next_index = '0' * (len(first_index) - len(next_index)) + next_index
        next_url = urllib.parse.urljoin(url_head, re.sub(first_index, next_index, url_tail))
        try:
            output_file = os.path.join(output_dir, os.path.basename(next_url))
            urllib.request.urlretrieve(next_url, output_file)
            print('Successfully downloaded {}'.format(os.path.basename(next_url)))
        except IOError:
            print('Could not retrieve {}'.format(next_url))
        index_count += 1


if __name__ == '__main__':
    first_link = 'http://699340.youcanlearnit.net/image001.jpg'
    download_files(first_link, '.\\images')
