
################################################
How to use?
################################################


Running on Localhost
####################
Run the program on localhost in the following order.

Clone
*****
1. Use Git or checkout with SVN using the web URL. ::

      $ git clone https://github.com/Lainshower/Img3Sum.git


Run
***
1. Create conda environment and install packages ::

      $ conda env create --file requirements.yaml

2. Activate conda environment ::

      $ conda activate env

3.  Run [app.py](https://github.com/Lainshower/Img3Sum/blob/main/app.py) ::

      $ python app.py


Running each feature with python
################################

In this guide, we'll show you how to use Img3Sum.

- **If you want to extract text from an image**

.. code-block:: python

    from IMG3SUM.OCR_RUN import ocr_from_img
    text=ocr_from_img("image path")
    print(text)

- **If you want a summary from the text**

.. code-block:: python

    from IMG3SUM.extract import get_summary 
    eng_sum, kor_sum = get_summary(text)
    print(eng_sum)
    print(kor_sum)
    # You can get a summary of the Korean and English versions.

- **If you want a summary from the image**

.. code-block:: python

    from IMG3SUM.OCR_RUN import ocr_from_img
    from IMG3SUM.extract import get_summary 
    text=ocr_from_img("image path")
    eng_sum, kor_sum = get_summary(text)
    print(eng_sum)
    print(kor_sum)

Hosting with External URL
#########################