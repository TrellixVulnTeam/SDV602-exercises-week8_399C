import tarfile

def create_tar_archive():
  files = ['monsters.csv','Monster_contact_sheet.pdf']

  with tarfile.open('archive.tar','w') as tar:
    for file in files:
      tar.add(file)


def add_to_tar_archive():
  with tarfile.open('archive.tar','a') as tar:
    tar.add('monsters_card03.png')


def extract_tar():
  with tarfile.open('archive.tar') as tar:
    tar.extract('monsters_card03.png')


def extract_all():
  with tarfile.open('archive.tar') as tar:
    tar.extractall('extracted_monster_files')


if __name__ == "__main__":
  extract_all()