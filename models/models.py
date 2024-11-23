from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(255), nullable=False)  # Hash the password later
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    gender = db.Column(db.String(20), nullable=False)  # 0 for Female, 1 for Male
    role = db.Column(db.Integer, nullable=False)  # 0 for User, 1 for Admin
    status = db.Column(db.Integer, nullable=False)  # 1 for Active, 0 for Inactive
    address = db.Column(db.Text, nullable=True)
    profile = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'code': self.code,
            'email': self.email,
            'phone': self.phone,
            'gender': self.gender,
            'role': self.role,
            'status': self.status,
            'address': self.address,
            'profile': self.profile
        }


class TempImage(db.Model):
    __tablename__ = 'temp_image'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Relationship to Product
    products = db.relationship('Product', back_populates='category')

    def to_dict(self, include_products=True):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
        if include_products:
            data['products'] = [product.to_dict(include_category=False) for product in self.products]
        return data


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(100), nullable=False)

    # Foreign key to Category
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    cost = db.Column(db.Numeric(10, 2), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    current_stock = db.Column(db.Integer, default=0)

    # Relationship to Category
    category = db.relationship('Category', back_populates='products')

    def to_dict(self, include_category=True):
        data = {
            'id': self.id,
            'code': self.code,
            'image': self.image,
            'name': self.name,
            'category_id': self.category_id,
            'cost': str(self.cost),
            'price': str(self.price),
            'current_stock': self.current_stock
        }
        if include_category and self.category:
            data['category'] = self.category.to_dict(include_products=False)  # Prevent recursion in category
        return data
