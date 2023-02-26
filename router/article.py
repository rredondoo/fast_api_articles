from typing import List
from schemas import ArticleBase, ArticleDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from auth.oauth2 import oauth2_schema


router = APIRouter(
    prefix='/article',
    tags=['article']
)


# create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(request, db)


# get specific article
@router.get('/{article_id}', response_model=ArticleDisplay)
def get_article(article_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    return db_article.get_article(id, db)
