import struct
def read_chunk(file):
    """Read and return a chunk identifier and its size."""
    chunk_id = file.read(4)
    if not chunk_id:
        return "", 0  # End of file
    chunk_size = int.from_bytes(file.read(4), byteorder='little')
    return chunk_id.decode('ascii'), chunk_size

def read_list_chunk_contents(file, chunk_size):
    """Read and print the contents of the LIST chunk."""
    end_of_chunk = file.tell() + chunk_size
    while file.tell() < end_of_chunk:
        sub_chunk_id, sub_chunk_size = read_chunk(file)
        print(f"Found sub-chunk {sub_chunk_id} of size {sub_chunk_size}")
        
        # 读取子块内容
        sub_chunk_data = file.read(sub_chunk_size)
        print(len(sub_chunk_data).to_bytes(4, 'little'))
        print(sub_chunk_data)
        return sub_chunk_data

def find_info_or_list_chunks(file_path):
    """Find and print out INFO or LIST chunks from a WAV file, including LIST contents."""
    with open(file_path, 'rb') as file:
        # Skip the RIFF header
        file.read(12)  # 'RIFF', size, 'WAVE'
        while True:
            chunk_id, chunk_size = read_chunk(file)
            if chunk_id == 'LIST':
                print(f"{chunk_id} size:{chunk_size}")
                # read_list_chunk_contents(file, chunk_size)
            elif chunk_id == "":
                break  # End of file reached
            else:
                print(f"{chunk_id} size:{chunk_size}")
                file.seek(chunk_size, 1)  # Skip this chunk
# 打开WAV文件
file_2 = r" "
# 打开文件
with open(file_2, 'rb') as f:
    header = f.read(64)

# 解析RIFF头部结构
if header.startswith(b'RIFF'):
    _, file_size, file_type = struct.unpack('4sI4s', header[:12])
    print(f"File Size: {file_size}, File Type: {file_type.decode()}")

# 替换为您的WAV文件路径
file_path = file_2

find_info_or_list_chunks(file_path)
print("over")