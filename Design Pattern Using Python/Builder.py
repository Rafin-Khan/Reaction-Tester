class Builder:
  _build = None

  def attacher(self, attach):
    self._build = attach

  def make_robot(self):
    robot = Robot()

    #Get Body
    body = self._build.getBody()
    robot.setBody(body)

    #Attach head
    head = self._build.getHead()
    robot.attachHead(head)

    #Attach arms and legs
    for i in range(2):
      arm = self._build.getArms()
      leg = self._build.getLegs()
      robot.attachArms(arm)
      robot.attachLegs(leg)
    
    return robot


class Robot:
  _head = None
  _body = None
  _arms = []
  _legs = []

  def setBody(self, body):
    self._body = body

  def attachHead(self, head):
    self._head = head

  def attachArms(self, arm):
    self._arms.append(arm)

  def attachLegs(self, leg):
    self._legs.append(leg)

  def specs(self):
    print("Big Robot")
    print("-------------------------")
    print("Body Girth: {}".format(self._body.girth))
    print("Head Shape: {}".format(self._head.shape))
    print("Number of arms: {}".format(len(self._arms)))
    print("NUmber of legs: {}".format(len(self._legs)))



class Attach:

  def getHead(self):
    head = Head()
    head.shape = "Round"
    return head

  def getArms(self):
    arms = Arms()
    arms.size = "Big"
    return arms

  def getLegs(self):
    legs = Legs()
    legs.length = "Long"
    return legs

  def getBody(self):
    body = Body()
    body.girth = "Fat"
    return body


class Head:
  shape = None

class Arms:
  size = None

class Legs:
  length = None

class Body:
  girth = None


def main():
   attach = Attach()
   
   builder = Builder()
   
   
   
   builder.attacher(attach)
   robot = builder.make_robot()
   robot.specs()

if __name__ == "__main__":
   main()
