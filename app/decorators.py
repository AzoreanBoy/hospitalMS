from django.shortcuts import redirect


def unauthenticatedUser(viewFunc):
    def wrapperFunc(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return viewFunc(request, *args, **kwargs)

    return wrapperFunc
