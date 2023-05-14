from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 특정 객체를 접근할 때 사용되는 권한(get, update, delete) <-> APIView 기반의 POST에서는 호출되지 않음
        # GET, HEAD, OPTIONS 요청은 항상 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 작성자만 수정, 삭제를 허용
        return obj.user == request.user
