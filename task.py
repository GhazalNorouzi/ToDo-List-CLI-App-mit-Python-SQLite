import sqlite3

from db import get_connection


# کلاس Task
class Tasks:
    def __init__(self, title, description, status = 'pending', id = None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    # تغییر وضعیت تسک
    def change_status(self, new_status):
        self.status = new_status

    # ذخیره کردن تسک در دیتابیس
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?, ?)",
            (self.id, self.title, self.description, self.status)
        )
        conn.commit()
        conn.close()

    # بروزرسانی تسک
    def update(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?",
            (self.title, self.description, self.status, self.id)
        )
        conn.commit()
        conn.close()

    # حذف تسک
    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    # دریافت تسک بر اساس id
    @classmethod
    def get_by_id(cls, task_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[0], row[1], row[2], row[3])
        return None

    # دریافت همه تسک‌ها
    @classmethod
    def get_all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, description, status FROM tasks")
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            task = cls(row[0], row[1], row[2], row[3])
            tasks.append(task)
        conn.close()
        return tasks
