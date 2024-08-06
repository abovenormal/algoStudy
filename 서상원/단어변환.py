
from collections import deque
def solution(begin, target, words):
    answer = 0
    
    def find_words(now,visited):
        li=[]
        len_=len(now)
        
        for word in words:
            chance=0
            if word not in visited: # 방문 안했고 
                for idx in range(len_): # 글자 수 체크 
                    if now[idx]!=word[idx]:
                        chance+=1
                    if chance>=2:
                        break
                if chance==1: # 1자만 틀린 단어
                    li.append(word)
        return li
                    
                    
                    
    
    
    
    def bfs(begin,target):
        visited=set()
        visited.add(begin)
        q=deque([(begin,0)]) # word , cnt
        
        while q:
            now , cnt= q.popleft()
            
            if now == target: # 정답 조건 
                return cnt 
            
            change_words=find_words(now,visited) # 아직 방문하지 않았고 현재 단어에서 변환 가능한 단어 리스트들 return
            
            
            for next in change_words:
                if next not in visited:
                    q.append((next,cnt+1))
            

    if (target in words):
        answer=bfs(begin,target)
    else:
        answer=0
    
    
    return answer
