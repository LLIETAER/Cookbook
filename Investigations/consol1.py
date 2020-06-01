from subprocess import Popen,PIPE


def subprocess_cmd(dr,cmd1,cmd2):
    p1 = Popen(cmd1.split(),stdout=PIPE,cwd=dr)
    p2 = Popen(cmd2.split(),stdin=p1.stdout,stdout=PIPE,cwd=dr)
    p1.stdout.close()
    return p2.communicate()[0]

subprocess_cmd('/Users/louislietaer/PycharmProjects/Investigations/venv/bin/',
               'open -a Terminal',
               '/Users/louislietaer/PycharmProjects/Investigations/venv/bin/python /Users/louislietaer/PycharmProjects/Investigations/cons.py')
