a = {10, 20, 30, 40}
b = {30, 40, 50}

a.add(60)
print("add:", a)
a.update([70, 80])
print("update:", a)
a.remove(80)
print("remove:", a)
a.discard(100)
print("discard:", a)
print("union:", a.union(b))
print("intersection:", a.intersection(b))
print("difference:", a.difference(b))
print("symmetric difference:", a.symmetric_difference(b))
print("issubset:", {30, 40}.issubset(b))
print("issuperset:", b.issuperset({30, 40}))
print("isdisjoint:", a.isdisjoint({100, 200}))
