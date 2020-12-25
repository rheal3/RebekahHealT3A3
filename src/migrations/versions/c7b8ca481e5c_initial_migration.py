"""Initial migration

Revision ID: c7b8ca481e5c
Revises: 
Create Date: 2020-12-26 06:41:49.470167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7b8ca481e5c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('playlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('playlist_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('playlist_name')
    )
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('artist', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('playlists_songs',
    sa.Column('playlist_id', sa.Integer(), nullable=True),
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlists.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], )
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('audio')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audio',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('audio_file', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='audio_pkey'),
    sa.UniqueConstraint('audio_file', name='audio_audio_file_key')
    )
    op.drop_table('profiles')
    op.drop_table('playlists_songs')
    op.drop_table('users')
    op.drop_table('songs')
    op.drop_table('playlists')
    # ### end Alembic commands ###
