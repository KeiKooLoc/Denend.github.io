If not provided, the current working directory is used.

    `format` is the archive format: one of "zip", "tar", or "gztar". Or any
    other registered format. If not provided, unpack_archive will use the
    filename extension and see if an unpacker was registered for that
    extension.

    In case none is found, a ValueError is raised.
    """
    if extract_dir is None:
        extract_dir = os.getcwd()

    if format is not None:
        try:
            format_info = _UNPACK_FORMATS[format]
        except KeyError:
            raise ValueError("Unknown unpack format '{0}'".format(format))

        func = format_info[1]
        func(filename, extract_dir, **dict(format_info[2]))
    else:
        # we need to look at the registered unpackers supported extensions
        format = _find_unpack_format(filename)
        if format is None:
            raise ReadError("Unknown archive format '{0}'".format(filename))

        func = _UNPACK_FORMATS[format][1]
        kwargs = dict(_UNPACK_FORMATS[format][2])
        func(filename, extract_dir, **kwargs)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ��?)+�
���G�������t3Λi[H�	�"��ha��&�z��iG��z(��M�
GJx�L&p�1��dI��� ��,� U=E�0~@�����	���*F犀   ��y  |�%͹������ϺI��U>w~�r��ܩ�?d�iOc��⮓�r(Dbn>��{>Q��!+�;��î���˻���[�^y����^ =/��4�e�S� o���;]ޚ�1'�%@<�x1>OOI�#AW}8�:�.��)�O�v9���w�y�]&V}��I���+ȅ@5��gpU���.�|����H!d��U�wr�C���B�����wF2/]�8.kۘ���O����oWY�n�,����z���p����{�:�ȔW\�ީq��U݆8!����qD�-A��.�.�_T�h�_���+�+w1�ř���E���s{������ߓu�������YD>z�}����/�;gUn~������4���_������CH�xu���/��f����I����]���fV�'`�6<\`�2"�_�e�<��60P���J�{����w
�m߹�tL�w��}ﯺ��ܓ���T��R����ϓrnw;��wyw�"��l�k��dTu�*��E��XV�i�S�،Ir,i��8���
l� ~G�l\NY:��@J�8����MwwM�=Ϻd7�ޓ�ܺ�K��u<��CFb�%��� �t��D��mp�(��w�}I�2n�/k����w��u���(:|�{�����Q�0��� r���*O��G���ｱ��ڢu������vY��RM����3�� �]�<���T�����Q�W�>��zW7���9�[HK��r9�D�@Z��tײd��p�.��uG]ݰ���4OH���NK�ۚ�3�[C��ؿwD2N�ݐY�!�Www~wwޗ�=շ��tC��t�R��u��dT��O_MrEL��b��O����:!#n']�z��
Zk�bqE*�~���=0֪�"����K�_wL-��]�P�.4�WB�1��F�@ix1��s��B�M�����Fʓ^!�J�D5s��Q
���m�'׃Q<�����o�<]P�y�0�.�?VY��]#]�'=k���	!�R������,B�8ޕ��bt��f�߆/�S	�A�K+��؜���d!D��]�LA$�[K��N�.�?Z���p\�0��t8��`1,���2�r<�!��G%榨`I3���w�br6RN6�b�x��)�4�HCPIBZ������D������w�A�5�.�8}�3�����6iK��g�ǎ��Mڵ6eRi��B,����g{�羝[c{'.��V,E��l�;@;)�{���6&�6y���,.��s��׮@�MwSsE\�S�L:*��w"�g���c�Z���g��O���$[cq��*��dɏ2�w�;���:��+����ʪ՝ɮ��xt��*�U5�k��\�S�u	���5# �@g�JNB�CHk^0zHj�l�+���ӊGnX�H1��D�  �! 1~;�  ��`81 3\� 3Q1r9�d���{�?�q.  � ����,,44$44666666:::>:::DDDHHDDDJJJNJJJLLLLLLPPPPP````ttt���     "   """"""$$$$$&&&&(*(**,  �� �    ��@  ���V,�%`hh���B��5��6�4
���{_6g2��I�{�������Xk�ׅL+��f�X`P��/,^���j����;�B����sֆ�' ��� T�^&bh i 0!q��'&8��h�G��v'{�!�^J�s�z�A"3���ȓ��

G�O�4�&?�>��P����/n|���X�ip�%�s�@� ]�xhq]�3����X v���{�Y�h���!�Z r>Xo�>O] 	C��{!����� �ҸU�9-A��-��� г�n�b���؃J7�E�@�v%$*�)$�u( �
�PŬa �֮� s���F ӂ� �C@"ϰ\`܀��p l��RB���e���D���Un �5#e��`@� XCl�*�G�?�3�  1�e$+�jo�.���'� b �4 
�a��@@M ���#�@b;��k��u��0v@0��o>�Ā���/z���H�����H�j�3X�aO�3>	!t��o���>�[p�@0��h3������ʎ�\ �����-�:�����'����	�����gb�����0�Z��9X�=*=��u@���g̀3d
95i:P�`�c��P�1: P��ʂQn��<}� �V
AL�&$ >X��H���4�����d�� ۄ�&Gp!�_��3���m�a1o��tv3<�&!��D"���¤��*�� �2 ��!��#XC ' ����v#%�ա���8�΢@�3��zP�� �n�
ɝ�[c           @   s"  d  Z  d d l Z d d l Z d d l Z d d l m Z d d l Z d d l Z d d l Z d d l	 m
 Z
 y d d l Z e Z Wn e k
 r� e Z n Xy d d l m Z Wn e k
 r� d Z n Xy d d l m Z Wn e k
 r� d Z n Xd d	 d
 d d d d d d d d d d d d d d d d d d g Z d e f d �  �  YZ d e f d �  �  YZ d e f d �  �  YZ d  e f d! �  �  YZ d" e f d# �  �  YZ y e Wn e k
 r�d Z n XdW d& � Z d' �  Z  d( �  Z! d) �  Z" d* �  Z# d+ �  Z$ d, �  Z% d- �  Z& e d e% e d. � Z' e d d/ � Z( d0 �  Z) d1 �  Z* d2 �  Z+ d3 �  Z, d4 �  Z- d5 d6 d6 d d d d7 � Z. e e d8 � Z/ d6 d6 d d9 � Z0 i e. dX g d; f d< 6e. dY g d> f d? 6e. dZ g d@ f dA 6e0 g  dB f dC 6Z1 e re. d[ g d> f e1 d? <n  dD �  Z2 d dE dF � Z3 dG �  Z4 d d d6 d6 d d d dH � Z5 dI �  Z6 dJ �  Z7 d dE dK � Z8 dL �  Z9 dM �  Z: dN �  Z; dO �  Z< i dP dQ g e< g  d; f d< 6dR g e< g  d@ f dA 6dS g e; g  dB f dC 6Z= e rdT g e< g  d> f e= d? <n  dU �  Z> d d dV � Z? d S(\   s�   Utility functions for copying and archiving files and directory trees.

XXX The functions here don't copy the resource fork or other metadata on Mac.

i����N(   t   abspathi   (   t   tarfile(   t   getpwnam(   t   getgrnamt   copyfileobjt   copyfilet   copymodet   copystatt   copyt   copy2t   copytreet   movet   rmtreet   Errort   SpecialFileErrort	   ExecErrort   make_archivet   get_archive_formatst   register_archive_formatt   unregister_archive_formatt   get_unpack_formatst   register_unpack_formatt   unregister_unpack_formatt   unpack_archivet   ignore_patternsc           B   s   e  Z RS(    (   t   __name__t
   __