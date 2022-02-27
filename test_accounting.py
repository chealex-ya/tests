from accounting import check_document_existance, get_doc_owner_name, delete_doc, add_new_doc
import unittest

# Следует протестировать основные функции по получению информации
# о документах, добавлении и удалении элементов из словаря.

#     ap - (all people) - команда, которая выводит список всех владельцев документов
#     p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
#     l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
#
#     a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
#     имя владельца и номер полки, на котором он будет храниться.

#     d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;

class Test_get_doc_owner_name(unittest.TestCase):
	def setUp(self):
		print("method set up")

	def tearDown(self):
		print("method tearDown")

	def test_name(self):
		self.assertEqual(get_doc_owner_name('2207 876234'), 'Василий Гупкин')

class Test_check_document_existance(unittest.TestCase):
	def setUp(self):
		print("method set up")

	def tearDown(self):
		print("method tearDown")

	def test_existance(self):
		self.assertTrue(check_document_existance('2207 876234'))

class Test_delete_doc(unittest.TestCase):
	def setUp(self):
		print("method set up")

	def tearDown(self):
		print("method tearDown")

	def test_delete(self):
		self.assertTrue(delete_doc('10006'))

class Test_add_new_doc(unittest.TestCase):
	def setUp(self):
		print("method set up")

	def tearDown(self):
		print("method tearDown")

	def test_add_new_doc(self):
		self.assertEqual(add_new_doc(1,'new type','new owner', 4), 4)



if __name__ == "__main__":
  unittest.main()