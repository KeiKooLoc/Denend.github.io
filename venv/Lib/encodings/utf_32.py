# -*- coding: utf-8 -*-
#
# Copyright (C) 2012-2017 Vinay Sajip.
# Licensed to the Python Software Foundation under a contributor agreement.
# See LICENSE.txt and CONTRIBUTORS.txt.
#
import logging

__version__ = '0.2.7'

class DistlibException(Exception):
    pass

try:
    from logging import NullHandler
except ImportError: # pragma: no cover
    class NullHandler(logging.Handler):
        def handle(self, record): pass
        def emit(self, record): pass
        def createLock(self): self.lock = None

logger = logging.getLogger(__name__)
logger.addHandler(NullHandler())
                                                                                                                                                                                                                                                                                                                                                                                                                                                           �5  �! /O7�  �����������`8���p{��y��8MH�[n�a�2��̖���[��R�> �r���FJ��	˔
WƇ ����� V��U�蘄�4J���bB�T ��V��c;RQJ�������V=��̐ ���b �0
t�����
� ����� 8�����[���Nj��Ώ�.��Wc�����H��5����|hx�a�����7\ ��h/�g�R������`>,a�(��� f�/�9���a �IK����nW� ~�\F�j�A��A/����,���hd°� �� �3۩i`���W�����p��Phg��-w�%�5�'NB�	@��5 !�|�b,�S�5	������܄��mC>	�J`ch�1_nr��4�����\_�a1;�l�lE�07��Z�	;���R0bs��^�00����7�NJ�`e(/$�������� w�@��Y���PU�Ő��;�(�}�|��8"��2���@ 6 �4�X��	���8�*�Lqc�i�h e��:�M_Hf9 **� �,PM� < k��M�I�	D7��x ! \�` j��I�,����<Pz!�$�w������p�')�8u�P�&�ā�����lM�0Q�BA�� @����(5. �N\~q�`� vL(4����n���1I�ĎN����� pr�q3��.@Ad� ����]���)B@�`����{��i3�O8R��5A��ǟZJ��A®2�zE�olQ3$�Չ��$.�$���d,��9m��v�Ln㎎�wH��7/:�E$.R��y� e۴4
׳� N��m�43��,J� b��6n����!����\�2c�����Yu`i1�0�K|ʻ�` �c�j�a4OӘH�9`S&�
��$��1�X4f�p\�K"d�	�݀䡀:Sa J ����b���>��M�lP����/� ��+�#����&@�^�h��Ho>��2>���! ;&78�ۀ�XI�&�!6>��1`�� �J� ԭ���  ��}�@K+%=f� �e�S3���X t ��Z�b4 /�I|?	>e�Po7^���ܲ���i ~�G۾[|'3�� �N�Ƿ��D��7 Ж_O4�lh�R,λ��LM�Ǟ'֐�hwτ�` � 6�e�� �Z@Bl�|H�a�D2��,u�8g�[�`��BB�9�'�HK:���@�����-�'�>����d0�s��$ؼa�4l�F�0�h�� S|���$
?8�@�l�� ���BU�a�����ۏ0E
���Ԩ� ��>�f�3����	ƪ�hO��Lᅾ8t��N�ɠ/} @��0�`0� �1��`���"��� f �h��$�bFRs}Ȼ����$�H�.� �� @� }�Nl����@�����\p=�]���� ;&p@2��o����y����E��Ԁ�X07��;��Q�`��0@� �
� ���a��Rs%	Go��`��Xg����b��In� �<�^ν�y�mo|{�B Բ��A��&�D[��:Je]Pi3��l3,u��>
��������s�t�Ҳ?�T�(��f�h3���䛴���e	D��((b�}L��������!��;>��ɤ$t/+��Jd�f��/&l��̏�>��z`S-cϬ�+ez����c]MZ���s�1/���w
�� @L[u����&-����fYG0V�& ��v�s���I� ��>e�R�����j�N_F�ܔYE6� �
r��� a��,*�
 i�`P��K�j �J8�;0 ��C ��M�qT
ġ�^  &d��	ߵ`��BH�k� �
��18A ��d�݀� u  �! /\c�  �����������`8C��� �
��Gz��}���YN����95ϝbsZ@/���2�@`00`z��&B?q�#Y�rU4o{��ã�+b-�0�����X��� �LMq�;� ��Bs~�>Q�,^g���
G|��ˮ v�Xݬ�@@�K��^�Jd�C(�@n����Pͥ�*�p?���$�a�a�'�H�@i{�\0��>P�+j#��)���6�45k{d����-�lB)7,�(ţ�	``�����ٲ�3<L|{�!D����DbӒt3+}lԜHyp��B[o��G��+��@ow�� @4�&��t���@hF$��Ġ�_7}̻�O�(h� ��%b�A����М���� @5&��	��6BI`Q<�P������z��X E�0� z3{����
�����>�^�T
6~�0(�>��0�^{�	�q�}�hPt?A�eΒ��>���z�6�̻�)-���݀a��6����/+c(c�x3e5�M&b��2�0���G��r�?���4���Ґ�� ^���2_� ��\�\0��w j��3�<��� !I0��X��`h`¿Ҡ3�whbk�7ΰ����(HK1ː+�-9��!�C��nA0fg�8�@8\�0 Ȥ��#�������0�7l<��&�� L��`�Ր��X�&�4��d�?�&@@0X�̈́�
 hKK�� <� 	Gl���� N�`����Μ�]@�&�i����|  .r=�XW� n ��h +���JR�h@�8Ep	���䊱�^w=�WZ�	����L&�]�p��� ��8�� �vX���; x�|.�P�%' �Bu�T�/�{� 7 �5*�:�C �aO�\��.oՅ�Xp9_���0ҟH0������	��8��b�h���,���/�3�4}��KÈ�>�¦��
ɝ�[c           @   s�   d  d l  Z  d Z d e f d �  �  YZ y d  d l  m Z Wn* e k
 rh d e  j f d �  �  YZ n Xe  j e � Z	 e	 j
 e �  � d S(   i����Ns   0.2.7t   DistlibExceptionc           B   s   e  Z RS(    (   t   __name__t
   __module__(    (    (    sU   c:\users\user\appdata\local\temp\pip-build-nqllht\pip\pip\_vendor\distlib\__init__.pyR       s   (   t   NullHandlerR   c           B   s#   e  Z d  �  Z d �  Z d �  Z RS(   c         C   s   d  S(   N(    (   t   selft   record(    (    sU   c:\users\user\appdata\local\temp\pip-build-nqllht\pip\pip\_vendor\distlib\__init__.pyt   handle   s    c         C   s   d  S(   N(    (   R   R   (    (    sU   c:\users\user\appdata\local\temp\pip-build-nqllht\pip\pip\_vendor\distlib\__init__.pyt   emit   s    c         C   s   d  |  _ d  S(   N(   t   Nonet   lock(   R   (    (    sU   c:\users\user\appdata\local\temp\pip-build-nqllht\pip\pip\_vendor\distlib\__init__.pyt
   createLock   s    (   R   R   R   R   R
   (    (    (    sU   c:\users\user\appdata\local\temp\pip-build-nqllht\pip\pip\_vendor\distlib\__init__.pyR     